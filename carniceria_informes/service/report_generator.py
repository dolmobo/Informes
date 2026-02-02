from reportlab.lib import colors
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

from data.data_source import DataSource

class ReportService:

    def reporte_carniceria(db_path):
        rows = DataSource.obtener_carnes()
        total, suma_kg = DataSource.suma_kg(rows)

        #Config PDF
        doc = SimpleDocTemplate(db_path, pagesize= A4)
        styles = getSampleStyleSheet()
        elementos = []

        #Titulo
        title = f"<b>INFORME DE CARNICERIA</b>"
        elementos.append(Paragraph(title, styles['Title']))
        elementos.append(Spacer(1,20))

        #Fecha
        fecha = f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}"
        elementos.append(Paragraph(fecha, styles['Normal']))
        elementos.append(Spacer(1, 20))

        #Tabla
        data = [["Carne", "Tipo", "Peso"]]
        for r in rows:
            data.append([ r["carne"], r["tipo"], str(r["peso"]) ])

        table = Table(data)

        #Estilo
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.chocolate),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER')
        ])

        table.setStyle(style)
        elementos.append(table)
        elementos.append(Spacer(1, 20))

        #Texto resumen
        text = f"Total de carnes: <b> {total} </b> <br/> Peso total (kg): <b> {suma_kg} </b>"
        elementos.append(Paragraph(text, styles['Normal']))
        elementos.append(Spacer(1,20))

        doc.build(elementos)