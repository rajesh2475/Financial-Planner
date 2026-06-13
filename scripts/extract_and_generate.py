#!/usr/bin/env python3
"""
Extract metadata from Excel files and generate realistic HTML calculator pages.
"""

import os
from pathlib import Path
from typing import Dict, List, Any
import openpyxl

PROJECT_ROOT = Path(__file__).resolve().parent.parent
EXCELS_DIR = PROJECT_ROOT / "app" / "excels"
TEMPLATES_DIR = PROJECT_ROOT / "templates"

def slugify(name: str) -> str:
    """Convert Excel filename to URL slug."""
    slug = name.lower()
    for char in [" ", "_", ".xlsx", ".xls", "(", ")", "&", "\'", '"']:
        slug = slug.replace(char, "-")
    return "-".join(part for part in slug.split("-") if part)

def title_case(name: str) -> str:
    """Convert Excel filename to title case."""
    name = name.replace(".xlsx", "").replace(".xls", "")
    return name.replace("_", " ").title()

def extract_excel_metadata(file_path: str) -> Dict[str, Any]:
    """Extract input cells, labels, and formulas from Excel file."""
    metadata = {
        "inputs": [],
        "outputs": [],
        "description": "",
        "sheets": []
    }
    
    try:
        wb = openpyxl.load_workbook(file_path)
        ws = wb.active
        metadata["sheets"] = [ws.title]
        
        # Scan all cells for patterns
        for row in ws.iter_rows(values_only=False):
            for cell in row:
                if not cell.value:
                    continue
                
                cell_val = str(cell.value).upper().strip()
                
                # Look for input indicators
                if any(keyword in cell_val for keyword in [
                    "LOAN AMOUNT", "INTEREST RATE", "TENURE", "PLANNED MONTHLY",
                    "YEARS OF INVESTMENT", "ANNUAL RETURN", "CURRENT AGE",
                    "RETIREMENT", "MONTHLY EXPENSE", "INFLATION", "INCOME",
                    "SALARY", "AGE", "RATE", "AMOUNT", "PERIOD", "INVESTMENT",
                    "RETURN", "EXPENSE", "PRINCIPAL", "EMI"
                ]):
                    label = str(cell.value).strip()
                    if label not in [inp["label"] for inp in metadata["inputs"]]:
                        metadata["inputs"].append({
                            "label": label,
                            "type": "number",
                            "placeholder": "Enter " + label.lower()
                        })
                
                # Look for output indicators
                if any(keyword in cell_val for keyword in [
                    "TOTAL", "RESULT", "VALUE AT", "CORPUS", "EMI", "PAYMENT",
                    "INTEREST PAID", "TAX", "GAIN", "FINAL VALUE", "SIP"
                ]):
                    label = str(cell.value).strip()
                    if label not in [out["label"] for out in metadata["outputs"]]:
                        metadata["outputs"].append({
                            "label": label,
                            "type": "currency"
                        })
        
        wb.close()
    except Exception as e:
        print("Warning: Could not extract metadata from " + str(file_path) + ": " + str(e))
    
    return metadata

def generate_calculator_html(file_name: str, metadata: Dict[str, Any]) -> str:
    """Generate HTML calculator page from Excel metadata."""
    slug = slugify(file_name)
    title = title_case(file_name)
    
    # Generate input fields HTML
    inputs_html = ""
    for i, inp in enumerate(metadata.get("inputs", [])[:10]):  # Limit to 10 inputs
        field_id = "input_" + str(i)
        label = inp["label"]
        field_type = inp["type"]
        placeholder = inp["placeholder"]
        inputs_html += '\n        <div class="form-group mb-3">\n          <label for="' + field_id + '" class="form-label">' + label + '</label>\n          <input type="' + field_type + '" class="form-control" id="' + field_id + '" name="input_' + str(i) + '" placeholder="' + placeholder + '">\n        </div>'
    
    # Generate output fields HTML
    outputs_html = ""
    for i, out in enumerate(metadata.get("outputs", [])[:8]):  # Limit to 8 outputs
        label = out["label"]
        outputs_html += '\n        <tr>\n          <th>' + label + '</th>\n          <td id="result_' + str(i) + '">-</td>\n        </tr>'
    
    # Build template as plain string
    func_name = slug.replace("-", "_")
    if func_name[0].isdigit():
        func_name = "_" + func_name
    
    template = '{% extends "base.html" %}\n'
    template += '{% block title %}' + title + '{% endblock %}\n\n'
    template += '{% block content %}\n'
    template += '<div class="container mt-4">\n'
    template += '  <div class="card shadow-sm mb-4">\n'
    template += '    <div class="card-header fw-semibold">' + title + '</div>\n'
    template += '    <div class="card-body">\n'
    template += '      <p>This calculator is automatically generated from the Excel workbook. Enter your inputs below to calculate results.</p>\n'
    template += '      \n'
    template += '      <form id="calcForm" method="POST">\n'
    template += '        <fieldset>\n'
    template += '          <legend class="mb-3">Input Values</legend>\n'
    template += inputs_html + '\n'
    template += '        </fieldset>\n'
    template += '        \n'
    template += '        <button type="submit" class="btn btn-primary">Calculate</button>\n'
    template += '        <button type="reset" class="btn btn-secondary">Clear</button>\n'
    template += '        <a href="{{ url_for(\'default_page\') }}" class="btn btn-outline-secondary">Back to Home</a>\n'
    template += '      </form>\n'
    template += '    </div>\n'
    template += '  </div>\n'
    template += '\n'
    template += '  {% if result %}\n'
    template += '  <div class="card shadow-sm">\n'
    template += '    <div class="card-header fw-semibold">Results</div>\n'
    template += '    <div class="card-body">\n'
    template += '      <table class="table table-bordered">\n'
    template += '        <tbody>\n'
    template += outputs_html + '\n'
    template += '        </tbody>\n'
    template += '      </table>\n'
    template += '    </div>\n'
    template += '  </div>\n'
    template += '  {% endif %}\n'
    template += '\n'
    template += '  {% if error %}\n'
    template += '  <div class="alert alert-danger">{{ error }}</div>\n'
    template += '  {% endif %}\n'
    template += '</div>\n'
    template += '\n'
    template += '<script>\n'
    template += '  document.getElementById("calcForm").addEventListener("submit", function(e) {\n'
    template += '    e.preventDefault();\n'
    template += '    const formData = new FormData(this);\n'
    template += '    const data = Object.fromEntries(formData);\n'
    template += '    fetch("{{ url_for(\'calculators.' + func_name + '_api\') }}", {\n'
    template += '      method: "POST",\n'
    template += '      headers: {"Content-Type": "application/json"},\n'
    template += '      body: JSON.stringify(data)\n'
    template += '    })\n'
    template += '    .then(res => res.json())\n'
    template += '    .then(result => {\n'
    template += '      if (result.success) {\n'
    template += '        console.log("Calculation result:", result);\n'
    template += '        alert("Calculation submitted. Check console for details.");\n'
    template += '      } else {\n'
    template += '        alert("Error: " + (result.error || "Calculation failed"));\n'
    template += '      }\n'
    template += '    })\n'
    template += '    .catch(err => {\n'
    template += '      console.error("API error:", err);\n'
    template += '      alert("Failed to calculate: " + err.message);\n'
    template += '    });\n'
    template += '  });\n'
    template += '</script>\n'
    template += '{% endblock %}\n'
    
    return template

def main():
    """Generate realistic calculator pages from Excel files."""
    excel_files = sorted([
        f for f in os.listdir(EXCELS_DIR)
        if f.lower().endswith((".xlsx", ".xls"))
    ])
    
    print("Extracting metadata from " + str(len(excel_files)) + " Excel files...")
    
    success_count = 0
    for file_name in excel_files:
        file_path = EXCELS_DIR / file_name
        slug = slugify(file_name)
        template_path = TEMPLATES_DIR / (slug + ".html")
        
        try:
            # Extract metadata
            metadata = extract_excel_metadata(str(file_path))
            
            # Generate HTML
            html = generate_calculator_html(file_name, metadata)
            
            # Write template
            with open(template_path, "w", encoding="utf-8") as f:
                f.write(html)
            
            success_count += 1
            print("  OK " + slug + ".html (" + str(len(metadata['inputs'])) + " inputs, " + str(len(metadata['outputs'])) + " outputs)")
        except Exception as e:
            print("  ERROR " + slug + ": " + str(e))
    
    print("\nGenerated " + str(success_count) + "/" + str(len(excel_files)) + " calculator pages!")

if __name__ == "__main__":
    main()
