from datetime import datetime

from data.data_source import DataSource

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

class ReportService:
    def encabezado_pie(canvas: Canvas, doc):
        canvas.saveState()
        ancho, alto = A4
        fecha = datetime.now().strftime("%d/%m/%Y")

        canvas.drawImage("logo.png", 2.5*cm, alto - 3*cm, width= 2.5*cm, height=2.5*cm)

        canvas.setFont("Helvetica-Bold", 12)
        canvas.drawString(5*cm, alto - 2*cm, "INFORME DE EMPLEADOS")

        canvas.setFont("Helvetica", 9)
        canvas.drawString(5*cm, alto - 2.5*cm, "Autor: Dept. RRHH")

        canvas.drawRightString(ancho - 3*cm, alto - 2.5*cm, f"Fecha: {fecha}")

        canvas.setLineWidth(1)
        canvas.line(3*cm, alto - 3*cm, ancho - 3*cm, alto - 3*cm)

        #Pie
        canvas.line(3*cm, 3*cm, ancho - 3*cm, 3*cm)

        canvas.setFont("Helvetica", 9)
        canvas.drawString(3*cm, 2.5*cm, "Empresa S.L")

        canvas.setFont("Helvetica", 9)
        canvas.drawRightString(ancho - 3*cm, 2.5*cm, f"Pagina: {doc.page}")

        canvas.restoreState()

    def informe_empleados(file_path):
        #Config
        doc = SimpleDocTemplate(file_path, pagesize = A4)
        styles = getSampleStyleSheet()
        elementos = []

        datos = DataSource.obtener_informacion()

        elementos.append(Spacer(1, 0.5*cm))
        elementos.append(Paragraph("Informe de pelados con exceso de horas (Convenio > 40)", styles["BodyText"]))
        elementos.append(Spacer(1, 0.5*cm))

        datos_tabla = [[ "Nombre", "Departamento", "Total (h)", "Exceso (h)" ]]

        for r in datos:
            datos_tabla.append([ r["nombre"], r["departamento"], r["total"], r["exceso"] ])

        table = Table(datos_tabla)

        table.setStyle(TableStyle([
            ("BACKGROUND" ,(0,0),(-1,0), colors.burlywood),
            ("TEXTCOLOR",(0,0), (-1,0), colors.white),
            ("FONTNAME", (0,0),(-1,0), "Helvetica-Bold"),
            ("GRID", (0,0),(-1,-1), 1, colors.black),
            ("ALIGN", (0,0),(3,-1), "CENTER"),
            ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.gray, colors.black]),
            ("TEXTCOLOR", (0,1), (-1,-1), colors.white)
        ]))

        elementos.append(table)
        doc.build(
            elementos,
            onFirstPage=ReportService.encabezado_pie,
            onLaterPages=ReportService.encabezado_pie
        )