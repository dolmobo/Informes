from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from datetime import datetime
from data.data_source import DataSource

class ReportService:
    
    def encabezado_y_pie(canvas, doc):
        canvas.saveState()
        width, height = A4
        fecha = datetime.now().strftime("%d/%m/%Y")
        
        try:
            canvas.drawImage("logo.png", doc.leftMargin, height - 3 * cm, width=2.5*cm, height=2.5*cm, mask='auto')
        except:
            pass # Si no hay logo, no hacemos nada

        canvas.setFont("Helvetica-Bold", 12)
        canvas.drawString(doc.leftMargin + 3 * cm, height - 2 * cm, "INFORME DE HORAS EXTRA")

        canvas.setFont("Helvetica", 10)
        canvas.drawString(doc.leftMargin + 3 * cm, height - 2.6 * cm, "Autor: Dept. RRHH")
        canvas.drawRightString(width - doc.rightMargin, height - 2.6 * cm, f"Fecha: {fecha}")

        # Línea separadora encabezado
        canvas.line(doc.leftMargin, height - 3.2 * cm, width - doc.rightMargin, height - 3.2 * cm)

        # --- PIE DE PÁGINA ---
        # Línea separadora pie
        canvas.line(doc.leftMargin, 2.5 * cm, width - doc.rightMargin, 2.5 * cm)
        
        canvas.setFont("Helvetica", 8)
        canvas.drawString(doc.leftMargin, 1.8 * cm, "Empresa Inventada S.L. · Albacete")
        canvas.drawRightString(width - doc.rightMargin, 1.8 * cm, f"Página {doc.page}")

        canvas.restoreState()

    def generar_reporte(file_path):
        datos = DataSource.obtener_informe_horas()

        # Configuración del PDF con márgenes para dejar sitio al encabezado
        doc = SimpleDocTemplate(
            file_path,
            pagesize=A4,
            topMargin=3.5*cm,    # Margen superior amplio para el logo
            bottomMargin=3*cm,   # Margen inferior amplio para el pie
            leftMargin=2*cm,
            rightMargin=2*cm
        )

        styles = getSampleStyleSheet()
        elementos = []

        elementos.append(Spacer(1, 0.5 * cm))
        elementos.append(Paragraph("Trabajadores con exceso de horas (Convenio > 40h)", styles["BodyText"]))
        elementos.append(Spacer(1, 0.5 * cm))

        # Crear datos para la tabla
        tabla_datos = [["Nombre", "Departamento", "Total (h)", "Exceso (h)"]]
        
        for fila in datos:
            tabla_datos.append([ fila["nombre"], fila["departamento"], fila['total'], fila['exceso']])

        # Crear tabla y estilos
        tabla = Table(tabla_datos, colWidths=[6*cm, 5*cm, 3*cm, 4*cm])
        tabla.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
            ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
            ("ALIGN", (2,1), (-1,-1), "CENTER"), # Centrar columnas numéricas
            ("ALIGN", (0,0), (-1,-1), "CENTER"), # Centrar todo un poco más
        ]))

        elementos.append(tabla)

        # GENERAR PDF usando la función de encabezado
        doc.build(
            elementos, 
            onFirstPage=ReportService.encabezado_y_pie, 
            onLaterPages=ReportService.encabezado_y_pie
        )