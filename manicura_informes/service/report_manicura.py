from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

from datetime import datetime

from data.data_source import DataSource

class ReportManicura:
    def reporte_manicura(db_path):
        rows = DataSource.obtener_manicura()
        total, suma_precio = DataSource.suma_precios(rows)

        #CONFIG PDF
        doc = SimpleDocTemplate(db_path, pagesize = A4)
        styles = getSampleStyleSheet()
        elementos = []

        # Titulo
        text = "<b>INFORME DE MANICURA</b>"
        elementos.append(Paragraph(text, styles['Title']))
        elementos.append(Spacer(1, 20))

        #Fecha
        fecha = f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}"
        elementos.append(Paragraph(fecha, styles['Normal']))
        elementos.append(Spacer(1, 20))

        #Datos tabla
        data = [[ "Servicio", "Descripcion", "Precio" ]]
        for r in rows:
            data.append([ r["name"], r["descripcion"], str(r["precio"]) ])

        table = Table(data)

        # Estilo tabla

        style = TableStyle([
            ('BACKGROUND', (0, 0),(-1 ,0), colors.orange),
            ('FONTNAME', (0, 0),(-1 ,0), 'Helvetica-Bold'),
            ('TEXTCOLOR', (0, 0),(-1 ,0), colors.white),
            ('GRID', (0, 0),(-1 ,-1), 1, colors.black),
            ('ALIGN', (0, 0),(-1 ,-1), 'CENTER')
        ]) 

        table.setStyle(style)

        elementos.append(table)
        elementos.append(Spacer(1, 20))

        text = f"Servicios totales: <b> {total} </b>  <br/> Total precios: <b> {suma_precio} </b>"
        elementos.append(Paragraph(text, styles['Normal']))
        elementos.append(Spacer(1, 20))

        doc.build(elementos)