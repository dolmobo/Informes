from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

def build_participants_report(output_path, rows, summary, tittle = "Informe de participantes"):
    #Desempaquetamos la tupla summary en dos variables: total y suma de puntos
    total, points_sum = summary

    #Creamos una coleccion de estilos de ejmplo
    styles = getSampleStyleSheet()

    #Estilo personalizado para el titulo
    title_style = ParagraphStyle(
        "TituloPersonalizado",
        parent=styles["Title"],
        fontSize=18,
        leading=22, #Espacio entre lineas
        spaceAfter=6 #Espacio debajo del titulo
    )

    #Estilo de textos normales
    normal_styles = ParagraphStyle(
        "TextoPersonalizado",
        parent=styles["Normal"],
        fontSize=10,
        leading=13
    )

    # Configuracion del PDF
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin= 2.0 * cm,
        rightMargin= 2.0 * cm,
        topMargin= 2.0 * cm,
        bottomMargin = 2.0 * cm
    )

    story = []

    story.append(Paragraph(tittle, title_style))

    fecha_actual = datetime.now().strftime('%d/%m/%Y %H:%M')
    story.append(Paragraph(f"Fehca: {fecha_actual}", styles ["Normal"]))

    story.append(Spacer(1, 10))

    data = [["Nombre", "Departamento", "Puntos"]]

    for r in rows:
        data.append([str(r["name"]), str(r["department"]), str(int(r["points"]))  ])

    col_ancho = [8.5 * cm, 5.5 * cm, 2.5 * cm]

    table = Table(data, colWidths=col_ancho, hAlign="LEFT")

    style = TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1F4E79")),
        ("TEXTCOLOR", (0, 0),(-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN", (2, 1), (2, -1), "RIGHT"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),

    ])

    table.setStyle(style)
    story.append(table)

    story.append(Spacer(1, 14))

    story.append(Paragraph("<b>Resumen</b>", normal_styles))
    story.append(Paragraph(f"Total de participantes: <b>{total}</b>", normal_styles))
    story.append(Paragraph(f"Total de puntos: <b>{points_sum}</b>", normal_styles))

    doc.build(story)