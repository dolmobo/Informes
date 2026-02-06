from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem
from views.MainWindow_ui import Ui_MainWindow
from data.data_source import DataSource

from services.report_generator import ReportService

class MainController(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        DataSource.ensure_db()
        self.cargar_tabla()

        self.btnPDF.clicked.connect(self.generar_informe_control)

    def cargar_tabla(self):
        try:
            rows = DataSource.obtener_informacion()
            self.tableWidget.setRowCount(len(rows))

            for indice, datos in enumerate(rows):
                self.tableWidget.setItem(indice, 0, QTableWidgetItem(str(datos["nombre"])))
                self.tableWidget.setItem(indice, 1, QTableWidgetItem(str(datos["departamento"])))
                self.tableWidget.setItem(indice, 2, QTableWidgetItem(str(datos["fecha"])))
                self.tableWidget.setItem(indice, 3, QTableWidgetItem(str(datos["horas"])))
        except Exception as e:
            QMessageBox.critical(self, "ERROR", "No se ha podido cargar la tabla.")

    def generar_informe_control(self):
        try:
            file_path, _ = QFileDialog().getSaveFileName(self, "Guardando Informe de Jornadas", "ejercicio2_informe_jornadas.pdf", "PDF Files (*.pdf)")
            if file_path:
                ReportService.informe_control_horas(file_path)
                QMessageBox.information(self, "EXITO", "PDF generado con exito.")
        except Exception as e:
            QMessageBox.critical(self, "ERROR", f"No se ha podido general el PDF: {e}")