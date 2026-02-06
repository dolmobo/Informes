from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QFileDialog
from data.data_source import DataSource
from views.MainWindow_ui import Ui_MainWindow
from service.report_generator import ReportService

class MainController(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        DataSource.ensure_db()
        self.cargar_tabla()

        self.btnPDF.clicked.connect(self.generar_informe)

    def generar_informe(self):
        try:
            file_path, _ = QFileDialog().getSaveFileName(self, "Guardando Informe Empleados...", "empleados.pdf", "PDF Files (*.pdf)")
            if file_path:
                ReportService.informe_empleados(file_path)
                QMessageBox.information(self, "EXITO", "El pdf se ha generado con exito.")
        except Exception as e:
            QMessageBox.critical(self, "ERROR", f"No se ha podido genenar el PDF: {e}")

    def cargar_tabla(self):
        try:
            datos = DataSource.obtener_informacion()
            self.tableEmpleados.setRowCount(len(datos))

            for indice, datos in enumerate(datos):
                self.tableEmpleados.setItem(indice,0, QTableWidgetItem(str(datos["nombre"])))
                self.tableEmpleados.setItem(indice,1, QTableWidgetItem(str(datos["departamento"])))
                self.tableEmpleados.setItem(indice,2, QTableWidgetItem(str(datos["total"])))
                self.tableEmpleados.setItem(indice,3, QTableWidgetItem(str(datos["exceso"])))
        except Exception as e:
            QMessageBox.critical(self, "ERROR", f"No se ha podido cargar la tabla: {e}")