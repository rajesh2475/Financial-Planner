import os
from pathlib import Path
from flask import Blueprint, render_template, abort, jsonify, url_for, redirect

excel_bp = Blueprint("excel", __name__)

EXCEL_ROOT = Path(__file__).resolve().parent.parent / "excels"


def _slugify(file_name: str) -> str:
    slug = file_name.lower()
    for char in [" ", "_", ".xlsx", ".xls", "(", ")", "&", "\'", '"']:
        slug = slug.replace(char, "-")
    return "-".join(part for part in slug.split("-") if part)


def _load_excel_files():
    if not EXCEL_ROOT.exists():
        return []
    return sorted(
        [f for f in os.listdir(EXCEL_ROOT) if f.lower().endswith((".xls", ".xlsx"))]
    )


def _find_excel_by_slug(slug: str):
    for file_name in _load_excel_files():
        if _slugify(file_name) == slug:
            return file_name
    return None


def _excel_metadata(file_name: str):
    slug = _slugify(file_name)
    return {
        "name": file_name,
        "slug": slug,
        "page_url": url_for("excel.excel_detail", slug=slug),
        "api_url": url_for("excel.excel_api", slug=slug),
        "description": "Placeholder page for the calculator represented by this Excel file.",
    }


@excel_bp.route("/")
def excel_index():
    # Redirect from the Excel base URL to the home dashboard.
    return redirect(url_for("default_page"))


@excel_bp.route("/<slug>")
def excel_detail(slug):
    file_name = _find_excel_by_slug(slug)
    if not file_name:
        abort(404)
    return render_template("excel_detail.html", file_name=file_name, metadata=_excel_metadata(file_name))


@excel_bp.route("/<slug>/api")
def excel_api(slug):
    file_name = _find_excel_by_slug(slug)
    if not file_name:
        abort(404)
    return jsonify(_excel_metadata(file_name))


@excel_bp.route("/api")
def excel_list_api():
    files = _load_excel_files()
    return jsonify([_excel_metadata(f) for f in files])
