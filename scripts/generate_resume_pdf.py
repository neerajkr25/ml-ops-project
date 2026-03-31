"""Generate NeerajKumar_DevOps_Resume.pdf from NeerajKumar_DevOps_Resume.md (root)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    from fpdf import FPDF
except ImportError:
    print("Install fpdf2: py -m pip install fpdf2", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
MD = ROOT / "NeerajKumar_DevOps_Resume.md"
PDF = ROOT / "NeerajKumar_DevOps_Resume.pdf"


def strip_md(text: str) -> str:
    text = text.replace("\u2014", "-").replace("\u2013", "-")
    text = text.replace("\u00b7", " - ")
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = text.replace("#", "").strip()
    return text


def main() -> None:
    if not MD.exists():
        print(f"Missing {MD}", file=sys.stderr)
        sys.exit(1)

    raw = MD.read_text(encoding="utf-8")
    lines = raw.splitlines()

    pdf = FPDF()
    pdf.set_margins(left=15, top=15, right=15)
    pdf.set_auto_page_break(auto=True, margin=14)
    pdf.add_page()
    col_w = pdf.w - pdf.l_margin - pdf.r_margin
    # Core fonts are Latin-1; normalize non-ASCII for reliability
    def safe(s: str) -> str:
        return (
            s.encode("latin-1", errors="replace")
            .decode("latin-1")
            .replace("?", " ")
        )

    for line in lines:
        line = line.rstrip()
        if not line.strip():
            pdf.ln(3)
            continue
        if line.strip() == "---":
            pdf.ln(2)
            continue

        if line.startswith("# "):
            t = strip_md(line[2:])
            pdf.set_font("Helvetica", "B", 16)
            pdf.set_x(pdf.l_margin)
            pdf.multi_cell(col_w, 8, safe(t))
            pdf.ln(2)
            continue
        if line.startswith("## "):
            t = strip_md(line[3:])
            pdf.set_font("Helvetica", "B", 12)
            pdf.set_x(pdf.l_margin)
            pdf.multi_cell(col_w, 6, safe(t))
            pdf.ln(1)
            continue
        if line.startswith("### "):
            t = strip_md(line[4:])
            pdf.set_font("Helvetica", "B", 11)
            pdf.set_x(pdf.l_margin)
            pdf.multi_cell(col_w, 6, safe(t))
            pdf.ln(1)
            continue

        t = strip_md(line)
        pdf.set_font("Helvetica", "", 10)
        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(col_w, 5, safe(t))

    pdf.output(str(PDF))
    print(f"Wrote {PDF}")


if __name__ == "__main__":
    main()
