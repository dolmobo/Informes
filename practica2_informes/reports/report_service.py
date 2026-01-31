from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

from data.data_source import DataSource

class ReportService:
    
    def reporte_participantes(file_path):
        #Datos
        rows = DataSource.obtener_participants()
        total, suma = DataSource.suma_puntos(rows)

        #Config pdf
        doc = SimpleDocTemplate(file_path, pagesize=A4)
        elementos = []
        styles = getSampleStyleSheet()

        #TITULO
        title = Paragraph("<b>INFORME PARTICIPANTES</b>", styles['Title'])
        elementos.append(title)
        elementos.append(Spacer(1, 20))

        #DATOS TABLA
        data = [["Nombre", "Departamento", "Puntos"]]
        for r in rows:
            data.append([r["name"], r["department"], str(r["points"]) ])

        table = Table(data)

        #Estilo tabla
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTNAME', (0, 1), (-1, -1), 'Courier'),
            ('GRID', (0,0), (-1, -1), 1, colors.black)
        ])
        table.setStyle(style)

        elementos.append(table)
        elementos.append(Spacer(1,20))

        text = f"Total Participante: <b>{total}</b> <br/>  Puntos totales: <b>{suma}</b>"
        elementos.append(Paragraph(text, styles['Normal']))

        doc.build(elementos)

    def reporte_jugadores(file_path):
        #DATOS
        rows = DataSource.obtener_jugadores()
        total, suma = DataSource.suma_edad(rows)

        #Configurar PDF
        doc = SimpleDocTemplate(file_path, pagesize = A4)
        elementos = []
        styles = getSampleStyleSheet()

        #TITULO
        title = Paragraph("<b> INFORME JUGADORES </b>", styles['Title'])
        elementos.append(title)
        elementos.append(Spacer(1, 20))

        #DATOS TABLA
        data = [["Nombre", "Equipo", "Edad"]]
        for r in rows:
            data.append([ r["name"], r["team"], str(r["age"]) ])

        table = Table(data)

        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.orange),
            ('TEXTCOLOR', (0, 0), (-1 ,0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTNAME', (0, 1), (-1, -1), 'Courier'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])

        table.setStyle(style)
        elementos.append(table)
        elementos.append(Spacer(1, 20))

        text = f"Total jugadores: {total} <br/> Total edad: {suma}"
        elementos.append(Paragraph(text, styles['Normal']))

        doc.build(elementos)