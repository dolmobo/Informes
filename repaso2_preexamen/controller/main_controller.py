from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QFileDialog
from views.MainWindow_ui import Ui_MainWindow
from data.data_source import DataSource
from service.report_generator import ReportService

class MainController(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        DataSource.ensure_db()

        self.cargar_tabla()

        self.btnRefrescar.clicked.connect(self.cargar_tabla)
        self.btnPDF.clicked.connect(self.generar_informe)

    def generar_informe(self):
        try:
            file_path, _ = QFileDialog().getSaveFileName(self, "Guardando Informe Empleados...", "empleadosCAMBIADO.pdf", "PDF Files (*.pdf)")
            if file_path:
                ReportService.generar_informe(file_path)
                QMessageBox.information(self, "EXITO", "PDF generado con exito")

        except Exception as e:
            QMessageBox.critical(self, "ERROR", f"No se pudo generar el pdf: {e}")
    
    def cargar_tabla(self):
        try:
            rows = DataSource.obtener_informacion()
            total, suma_horas = DataSource.suma_horas(rows)

            self.tableEmpleados.setRowCount(len(rows))

            self.lblEstado.setText(f"Total de registros: {total} | Horas totales: {suma_horas}")

            for indice, datos in enumerate(rows):
                self.tableEmpleados.setItem(indice,0, QTableWidgetItem(str(datos["nombre"])))
                self.tableEmpleados.setItem(indice,1, QTableWidgetItem(str(datos["departamento"])))
                self.tableEmpleados.setItem(indice,2, QTableWidgetItem(str(datos["total"])))
                self.tableEmpleados.setItem(indice,3, QTableWidgetItem(str(datos["exceso"])))
        except Exception as e:
            QMessageBox.critical(self, "ERROR", f"No se ha podido cargar la tabla: {e}")