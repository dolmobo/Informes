from __future__ import annotations

from datetime import datetime
from typing import List, Dict, Tuple

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer


def build_participants_report(
    output_path: str,
    rows: List[Dict],
    summary: Tuple[int, int],
    title: str = "Informe de participantes",
) -> None:
    """Generate a professional PDF report using ReportLab Platypus.

    Mandatory elements:
    - SimpleDocTemplate
    - Table
    - TableStyle
    """
    total, points_sum = summary

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "TitleCustom",
        parent=styles["Title"],
        fontSize=18,
        leading=22,
        spaceAfter=6,
    )
    meta_style = ParagraphStyle(
        "MetaCustom",
        parent=styles["Normal"],
        fontSize=10,
        textColor=colors.grey,
        spaceAfter=12,
    )
    normal_style = ParagraphStyle(
        "NormalCustom",
        parent=styles["Normal"],
        fontSize=10,
        leading=13,
    )

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=2.0 * cm,
        rightMargin=2.0 * cm,
        topMargin=2.0 * cm,
        bottomMargin=2.0 * cm,
        title=title,
    )

    story = []
    story.append(Paragraph(title, title_style))
    story.append(Paragraph(f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}", meta_style))
    story.append(Spacer(1, 10))

    # Table data
    data = [["Nombre", "Departamento", "Puntos"]]
    for r in rows:
        data.append([str(r["name"]), str(r["department"]), str(int(r["points"]))])

    # Column widths (A4 usable width ~ 17cm with margins; keep it stable)
    col_widths = [8.5 * cm, 5.5 * cm, 2.5 * cm]

    table = Table(data, colWidths=col_widths, hAlign="LEFT")

    # Styling
    style = TableStyle([
        # Header (ampliación: destacar con color)
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1F4E79")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 10),
        ("ALIGN", (0, 0), (-1, 0), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 10),

        # Body
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), 10),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.whitesmoke, colors.lightgrey]),

        # Grid
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),

        # Padding
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 1), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 6),

        # Numeric alignment (ampliación: alinear a la derecha)
        ("ALIGN", (2, 1), (2, -1), "RIGHT"),
    ])
    table.setStyle(style)
    story.append(table)
    story.append(Spacer(1, 14))

    # Summary
    story.append(Paragraph("<b>Resumen</b>", normal_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph(f"Total de participantes: <b>{total}</b>", normal_style))
    story.append(Paragraph(f"Suma de puntos: <b>{points_sum}</b>", normal_style))

    doc.build(story)
