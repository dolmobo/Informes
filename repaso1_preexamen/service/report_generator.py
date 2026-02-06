from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.pdfgen.canvas import Canvas

from datetime import datetime

from data.data_source import DataSource

class ReportService:
    def encabezado_y_pie_jornada(canvas:Canvas, doc):
        canvas.saveState()
        ancho, alto = A4
        fecha = datetime.now().strftime("%d/%m/%Y")

        #Logo y titulo
        canvas.drawImage("logo.png", 2*cm, alto - 3*cm, width=2.5*cm, height=2.5*cm)

        canvas.setFont("Helvetica-Bold", 12)
        canvas.drawString(5*cm, alto - 1.8*cm, "INFORME DE JORNADAS")

        canvas.setFont("Helvetica", 10)
        canvas.drawString(5*cm, alto - 2.3*cm, "Autor: Dept. RRHH")

        #Fecha
        canvas.drawRightString(ancho - 2*cm, alto - 2.4*cm, f"Fecha: {fecha}")

        #Linea Cabecera
        canvas.setLineWidth(1)
        canvas.line(2*cm, alto - 3*cm, ancho - 2*cm, alto - 3*cm )

        #Pie de pagina
        canvas.line(2*cm, 3*cm, ancho - 2*cm, 3*cm)

        canvas.setFont("Helvetica", 8)
        canvas.drawString(2*cm, 2*cm, "Empresa S.L")
        canvas.drawRightString(ancho -2*cm, 1.8*cm, f"Pagina {doc.page}")

        canvas.restoreState()


    def encabezado_y_pie_empleados(canvas:Canvas, doc):
        canvas.saveState()
        ancho, alto = A4
        fecha = datetime.now().strftime("%d/%m/%Y")

        # 1. Logo y Título alineados (sin chocar)
        canvas.drawImage("logo.png", 2*cm, alto - 3*cm, width=2.5*cm, height=2.5*cm)
        
        canvas.setFont("Helvetica-Bold", 14)
        canvas.drawString(5*cm, alto - 1.8*cm, "INFORME DE HORAS") # Movido a la derecha
        
        canvas.setFont("Helvetica", 10)
        canvas.drawString(5*cm, alto - 2.4*cm, "Autor: Dept. RRHH")
        canvas.drawRightString(ancho - 2*cm, alto - 2.4*cm, f"Fecha: {fecha}")

        # 2. Línea horizontal recta (Separador)
        canvas.setLineWidth(1)
        # y1 y y2 deben ser iguales: alto - 3.2*cm
        canvas.line(2*cm, alto - 3.2*cm, ancho - 2*cm, alto - 3.2*cm)

        # 3. Pie de página
        canvas.line(2*cm, 2.5*cm, ancho - 2*cm, 2.5*cm)
        canvas.setFont("Helvetica", 8)
        canvas.drawString(2*cm, 1.8*cm, "Empresa S.L")
        canvas.drawRightString(ancho - 2*cm, 1.8*cm, f"Página {doc.page}")

        canvas.restoreState()

    def generar_reporte_empleados(file_path):
        #DATOS
        datos = DataSource.obtener_informe_horas()

        #Config PDF
        doc = SimpleDocTemplate(file_path, pagesize = A4)
        styles = getSampleStyleSheet()
        elementos = []

        elementos.append(Spacer(1, 0.5 * cm))
        elementos.append(Paragraph("Trabajadores con exceso de horas (Convenio > 40h)", styles["BodyText"]))
        elementos.append(Spacer(1, 0.5*cm))

        # Crear datos tabla
        tabla_datos = [[ "Nombre", "Departamento", "Total (h)", "Exceso (h)" ]]

        for fila in datos:
            tabla_datos.append([ fila["nombre"], fila["departamento"], fila["total"], fila["exceso"] ])

        # Crear tabla y estilos
        tabla = Table(tabla_datos)
        tabla.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), colors.black),
            ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
            ("GRID", (0,0), (-1,-1), 0.5, colors.black),
            ("ALIGN", (2,1), (-1,-1), "CENTER")
        ]))

        elementos.append(tabla)

        doc.build(
            elementos,
            onFirstPage=ReportService.encabezado_y_pie_empleados,
            onLaterPages=ReportService.encabezado_y_pie_empleados
        )
    
    def generar_reporte_jornadas(file_path):
        datos = DataSource.obtener_informe_jornadas()

        #Config PDF
        doc = SimpleDocTemplate(file_path, pagesize=A4)
        styles = getSampleStyleSheet()
        elementos = []

        elementos.append(Spacer(1, 0.5*cm))
        elementos.append(Paragraph("Jornadas", styles["BodyText"]))
        elementos.append(Spacer(1, 0.5*cm))

        tabla_datos = [[ "Nombre", "Departamento", "Fecha", "Horas" ]]

        for filas in datos:
            tabla_datos.append([ filas["nombre"], filas["departamento"], filas["fecha"], filas["horas"] ])

        tabla = Table(tabla_datos)
        tabla.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), colors.blueviolet),
            ("TEXTCOLOR", (0,0), (-1,0), colors.white),
            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
            ("GRID", (0,0), (-1,-1), 1, colors.black),
            ("ALIGN", (2,1), (-1,-1), "CENTER")
        ]))

        elementos.append(tabla)
        
        doc.build(elementos,
                  onFirstPage=ReportService.encabezado_y_pie_jornada,
                  onLaterPages=ReportService.encabezado_y_pie_jornada)