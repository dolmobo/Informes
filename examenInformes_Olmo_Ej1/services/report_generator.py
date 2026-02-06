from datetime import datetime
from data import data_source

from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

from data.data_source import DataSource

class ReportService:
    def encabezado_y_pie(canvas:Canvas, doc):
        canvas.saveState()
        ancho, alto = A4
        fecha = datetime.now().strftime("%d/%m/%Y")

        #ENCABEZADO
        canvas.drawImage("logo.png", 2*cm, alto - 3*cm, width=2.5*cm, height=2.5*cm)
        
        canvas.setFont("Helvetica-Bold", 12)
        canvas.drawString(5*cm, alto - 1.5*cm, "INFORME DE CONTROL DE HORAS")

        canvas.setFont("Helvetica", 9)
        canvas.drawString(5*cm, alto - 2*cm, "Autor: David Olmo Botey")

        canvas.drawRightString(ancho - 3*cm, alto - 2*cm, f"Fecha: {fecha}")

        canvas.line(1.5*cm, alto - 2.5*cm, ancho - 1.5*cm, alto - 2.5*cm)

        #PIE
        canvas.line(1.5*cm, 3*cm, ancho - 1.5*cm, 3*cm)

        canvas.setFont("Helvetica", 9)
        canvas.drawString(1.5*cm, 2.5*cm, "Innova Solutions S.L")

        canvas.setFont("Helvetica", 9)
        canvas.drawRightString(ancho - 1.5*cm, 2.5*cm, f"Pagina: {doc.page}")

        canvas.restoreState()

    def informe_control_horas(file_path):
        doc = SimpleDocTemplate(file_path, pagesize = A4)
        styles = getSampleStyleSheet()
        elementos = []

        datos = DataSource.obtener_informacion()

        elementos.append(Spacer(1, 0.2*cm))
        elementos.append(Paragraph("Informe para ver de forma ordenada, que ha trabajado cada empleado.", styles["BodyText"]))
        elementos.append(Spacer(1, 0.5*cm))

        datos_tabla = [[ "Nombre", "Departamento", "Total de horas semanales", "Maximo de horas en un dia", "Exceso de horas sobre 37.5" ]]
        
        for r in datos:
            datos_tabla.append([ r["nombre"], r["departamento"], r["total_semana"], r["max_dia"], r["exceso"] ])
        
        table = Table(datos_tabla)

        table.setStyle(TableStyle([
            ("BACKGROUND", (0,0),(-1,0), colors.chocolate),
            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
            ("TEXTCOLOR", (0,0), (-1,0), colors.white),
            ("ALIGN", (0,0), (-1,0), "CENTER"),
            ("GRID", (0,0),(-1,-1), 1, colors.black),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.lightyellow, colors.lightblue])
        ]))

        elementos.append(table)

        doc.build(elementos,
                  onFirstPage=ReportService.encabezado_y_pie,
                  onLaterPages=ReportService.encabezado_y_pie)