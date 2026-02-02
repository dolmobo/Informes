from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

from datetime import datetime

from data.data_source import DataSource

class ReportService:
    def reporte_ferreteria(db_path):
        rows = DataSource.obtener_repuestos()
        total, suma_precio = DataSource.suma_precio(rows)

        #CONFIG PDF
        doc = SimpleDocTemplate(db_path, pagesize= A4)
        styles = getSampleStyleSheet()
        elementos = []

        #Titulo
        text = "<b> INFORME DE FERRETERIA </b>"
        elementos.append(Paragraph(text, styles['Title']))
        elementos.append(Spacer(1, 20))

        #Fecha
        fecha = f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}"
        elementos.append(Paragraph(fecha, styles['Normal']))
        elementos.append(Spacer(1,20))

        #Cargar tabla
        data = [[ "Repuestos", "Descripcion", "Precio" ]]
        for r in rows:
            data.append([ r["repuesto"], r["descripcion"], str(r["precio"]) ])

        table = Table(data)

        #Estilos tabla
        style_table = TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.pink),
            ('FONTNAME', (0,0), (-1, 0), 'Helvetica-Bold'),
            ('TEXTCOLOR', (0,0), (-1, 0), colors.aquamarine),
            ('GRID', (0,0), (-1, -1), 1, colors.black),
            ('ALIGN', (0, 0), (2, -1), 'CENTER')
            ])
        

        table.setStyle(style_table)

        elementos.append(table)
        elementos.append(Spacer(1, 20))

        #Datos finales
        text = f"Total repuestos: <b> {total} </b>  <br/> Precio total: <b> {suma_precio} </b>"
        elementos.append(Paragraph(text, styles['Normal']))
        
        doc.build(elementos)