from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QFileDialog
from views.MainWindow_ui import Ui_MainWindow
from data.data_source import DataSource

from service.report_generator import ReportService

class MainController(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        DataSource.ensure_db()

        self.cargar_empleados()
        self.cargar_jornadas()

        self.btnRefrescarEmpleados.clicked.connect(self.cargar_empleados)
        self.btnRefrescarJornada.clicked.connect(self.cargar_jornadas)

        self.btnPDFEmpleados.clicked.connect(self.informe_empleados)
        self.btnPDF_Jornada.clicked.connect(self.informe_jornada)

    def informe_jornada(self):
        try:
            file_path, _ = QFileDialog().getSaveFileName(self, "Guardando Informe Jornada...", "jornada.pdf", "PDF Files (*.pdf)")
            if file_path:
                ReportService.generar_reporte_jornadas(file_path)
                QMessageBox.information(self,"EXITO", "PDF Generado con exito.")
        except Exception as e:
            QMessageBox.critical(self, "ERROR", f"No se ha podido generar el PDF: {e}")

    def informe_empleados(self):
        try:
            file_path, _ = QFileDialog.getSaveFileName(self, "Guardar Informe Empleados", "empleados.pdf", "PDF Files (*.pdf)")
            if file_path:
                ReportService.generar_reporte_empleados(file_path)
                QMessageBox.information(self, "EXITO", "PDF generado correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "ERROR", f"No se ha podido generar el PDF: {e}")

    def cargar_empleados(self):
        try:
            rowsHoras = DataSource.obtener_informe_horas()

            self.tableEmpleados.setRowCount(len(rowsHoras))


            for indice, dato in enumerate(rowsHoras):
                self.tableEmpleados.setItem(indice, 0, QTableWidgetItem(str(dato["nombre"])))
                self.tableEmpleados.setItem(indice, 1, QTableWidgetItem(str(dato["departamento"])))
                self.tableEmpleados.setItem(indice, 2, QTableWidgetItem(str(dato["total"])))
                self.tableEmpleados.setItem(indice, 3, QTableWidgetItem(str(dato["exceso"])))

        except Exception as e:
            QMessageBox.critical(self,"ERROR", f"No se pudo cargar la tabla empleados: {e}")

    def cargar_jornadas(self):
        try:
            rowsJornadas = DataSource.obtener_informe_jornadas()
            total, suma_precio = DataSource.suma_total(rowsJornadas)

            self.lblStatus_Jornada.setText(f"Numero de jornadas: {total} | Total horas: {suma_precio}")

            self.table_jornadas.setRowCount(len(rowsJornadas))

            for indice, dato in enumerate(rowsJornadas):
                self.table_jornadas.setItem(indice, 0, QTableWidgetItem(str(dato["nombre"])))
                self.table_jornadas.setItem(indice, 1, QTableWidgetItem(str(dato["departamento"])))
                self.table_jornadas.setItem(indice, 2, QTableWidgetItem(str(dato["fecha"])))
                self.table_jornadas.setItem(indice, 3, QTableWidgetItem(str(dato["horas"])))

        except Exception as e:
            QMessageBox.critical(self, "ERROR", f"No se pudo cargar la tabla jornadas: {e}")