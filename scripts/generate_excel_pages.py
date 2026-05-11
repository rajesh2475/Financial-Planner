#!/usr/bin/env python3
"""
Generate Flask routes and HTML templates for each Excel file in app/excels.
This script creates a separate page and route for each calculator.
"""

import os
import re
from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
EXCELS_DIR = PROJECT_ROOT / "app" / "excels"
ROUTES_FILE = PROJECT_ROOT / "app" / "routes" / "generated_calculators.py"
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

def load_excel_files():
    """Load all Excel files from the excels directory."""
    if not EXCELS_DIR.exists():
        return []
    return sorted([
        f for f in os.listdir(EXCELS_DIR) 
        if f.lower().endswith((".xls", ".xlsx"))
    ])

def generate_routes_file(files):
    """Generate Flask blueprint with routes for all Excel files."""
    routes_code = '''from flask import Blueprint, render_template, request, jsonify
from pathlib import Path

calc_bp = Blueprint("calculators", __name__)

# Auto-generated calculator routes
'''
    
    for file_name in files:
        slug = slugify(file_name)
        title = title_case(file_name)
        
        # Ensure function name is valid (no leading digits)
        func_name = slug.replace("-", "_")
        if func_name[0].isdigit():
            func_name = "_" + func_name
        
        routes_code += f'''
@calc_bp.route("/{slug}", methods=["GET", "POST"])
def {func_name}():
    """Calculator page for {file_name}."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "{slug}.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("{slug}.html", form={{}}, result=None)

@calc_bp.route("/{slug}/api", methods=["POST"])
def {func_name}_api():
    """API endpoint for {file_name}."""
    data = request.get_json() or {{}}
    return jsonify({{
        "file": "{file_name}",
        "slug": "{slug}",
        "title": "{title}",
        "status": "placeholder",
        "message": "Calculator API not yet implemented",
        "input_data": data
    }})
'''
    
    return routes_code

def generate_template(file_name: str):
    """Generate HTML template for a calculator."""
    slug = slugify(file_name)
    title = title_case(file_name)
    
    html = f'''{{%% extends "base.html" %%}}
{{%% block title %%}}{title}{{%% endblock %%}}

{{%% block content %%}}
<div class="card shadow-sm mb-4">
  <div class="card-header fw-semibold">{title}</div>
  <div class="card-body">
    <p><strong>Excel File:</strong> {file_name}</p>
    <p>This calculator is based on the Excel workbook: <code>{file_name}</code></p>
    
    <form method="POST" action="{{{{ url_for('calculators.{slug.replace("-", "_")}') }}}}">
      <div class="alert alert-info">
        <p><strong>Status:</strong> Placeholder page. Calculator logic not yet implemented.</p>
        <p>To implement this calculator, extract the logic from the Excel workbook and add form inputs and calculation methods.</p>
      </div>
      
      <div class="form-group">
        <label for="input1">Input 1</label>
        <input type="text" class="form-control" id="input1" name="input1" placeholder="Add form fields based on Excel workbook">
      </div>
      
      <button type="submit" class="btn btn-primary">Calculate</button>
      <a href="{{{{ url_for('default_page') }}}}" class="btn btn-secondary">Back to Home</a>
    </form>
  </div>
</div>

{{%% if error %%}}
<div class="alert alert-danger">
  {{{{ error }}}}
</div>
{{%% endif %%}}

{{%% if result %%}}
<div class="card shadow-sm">
  <div class="card-header fw-semibold">Results</div>
  <div class="card-body">
    <pre>{{{{ result | tojson(indent=2) }}}}</pre>
  </div>
</div>
{{%% endif %%}}

<script>
  // Fetch and display API metadata
  fetch("{{{{ url_for('calculators.{slug.replace("-", "_")}_api') }}}}", {{
    method: "POST",
    headers: {{"Content-Type": "application/json"}},
    body: JSON.stringify({{}})
  }})
  .then(res => res.json())
  .then(data => {{
    console.log("Calculator metadata:", data);
  }})
  .catch(err => console.error("API error:", err));
</script>
{{%% endblock %%}}
'''
    
    return html

def main():
    """Generate all calculator routes and templates."""
    files = load_excel_files()
    
    if not files:
        print("No Excel files found in app/excels")
        return
    
    # Generate routes file
    print(f"Generating routes for {len(files)} Excel files...")
    routes_code = generate_routes_file(files)
    
    with open(ROUTES_FILE, "w", encoding="utf-8") as f:
        f.write(routes_code)
    print(f"✅ Created {ROUTES_FILE}")
    
    # Generate templates
    print(f"Generating {len(files)} HTML templates...")
    for file_name in files:
        slug = slugify(file_name)
        template_path = TEMPLATES_DIR / f"{slug}.html"
        
        with open(template_path, "w", encoding="utf-8") as f:
            f.write(generate_template(file_name))
        print(f"  ✓ {slug}.html")
    
    print(f"\n✅ Generated all calculator pages!")
    print(f"\nNext steps:")
    print(f"1. Register the blueprint in app/__init__.py:")
    print(f"   from app.routes.generated_calculators import calc_bp")
    print(f"   app.register_blueprint(calc_bp, url_prefix='/calc')")
    print(f"\n2. Add navigation links in templates/base.html for specific calculators")

if __name__ == "__main__":
    main()
