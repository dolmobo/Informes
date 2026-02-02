from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

from data.data_source import DataSource

class ReportService:

    def reporte_fruteria(file_path):
        rows = DataSource.obtener_frutas()
        total, suma = DataSource.suma_peso(rows)

        #CONFIG PDF

        doc = SimpleDocTemplate(file_path, pagesize = A4)
        elementos = []
        styles = getSampleStyleSheet()

        #TITULO
        title = Paragraph("<b>INFORME DE FRUTERIA</b>", styles['Title'])
        elementos.append(title)
        elementos.append(Spacer(1, 20))

        #Datos Tabla
        data = [["Nombre", "Tipo", "Peso (KG)"]]
        for r in rows:
            data.append([ r["nombre"], r["tipo"], str(r["peso"]) ])

        table = Table(data)

        #Estilo tabla
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkgoldenrod),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('TEXTCOLOR', (0, 0), (-1, -0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ])

        table.setStyle(style)

        elementos.append(table)
        elementos.append(Spacer(1, 20))

        text = f"Total de fruta: {total} <br/> Peso total: {suma}"
        elementos.append(Paragraph(text, styles['Normal']))

        doc.build(elementos)