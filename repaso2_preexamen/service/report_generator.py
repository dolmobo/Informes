from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.pdfgen.canvas import Canvas

from data.data_source import DataSource

class ReportService:
    def encabezado_y_pie(canvas: Canvas, doc):
        canvas.saveState()
        ancho, alto = A4
        fecha = datetime.now().strftime("%d/%m/%Y")

        #Logo
        canvas.drawImage("logo.png", 2*cm, alto - 3*cm, height=2.5*cm, width=2.5*cm)

        #Titulos
        canvas.setFont("Helvetica-Bold", 12)
        canvas.drawString(5*cm, alto - 1.8*cm, "INFORME DE EMPLEADOS")

        canvas.setFont("Helvetica", 9)
        canvas.drawString(5*cm, alto- 2.4*cm, "Autor: Dept.  RRHH")

        canvas.drawRightString(ancho - 2*cm, alto - 2.4*cm, f"Fecha: {fecha}")

        canvas.setLineWidth(1)
        canvas.line(2*cm, alto - 3*cm, ancho - 2*cm, alto - 3*cm)

        #Pie de pagina

        canvas.line(2*cm, 3*cm, ancho - 2*cm, 3*cm)
        
        canvas.setFont("Helvetica", 9)
        canvas.drawString(2*cm, 2*cm,"Empresa S.L")
        canvas.drawRightString(ancho -2*cm, 2*cm, f"Pagina: {doc.page}")

        canvas.restoreState()

    def generar_informe(file_path):
        datos = DataSource.obtener_informacion()

        #CONFIG PDF
        doc = SimpleDocTemplate(file_path, pagesize=A4)
        styles = getSampleStyleSheet()
        elementos = []

        elementos.append(Spacer(1, 0.5*cm))
        elementos.append(Paragraph("Trabajadores con exceso de horas (Convenio > 40)"))
        elementos.append(Spacer(1, 0.5*cm))

        datos_tabla = [[ "Nombre", "Departamento", "Total (h)", "Exceso (h)" ]]

        for r in datos:
            datos_tabla.append([ r["nombre"], r["departamento"], r["total"], r["exceso"] ])
        
        table = Table(datos_tabla)

        table.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), colors.pink),
            ("TEXTCOLOR", (0,0), (-1,0), colors.gray),
            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
            ("GRID", (0,0), (-1,-1), 1, colors.black),
            ("ALIGN", (0,0), (-1,-1), "CENTER")
        ]))

        elementos.append(table)
        
        doc.build(
            elementos,
            onFirstPage=ReportService.encabezado_y_pie,
            onLaterPages=ReportService.encabezado_y_pie
        )