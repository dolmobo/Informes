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
    
    def cargar_tabla(self):
        try:
            rows = DataSource.obtener_informe_horas()
            
            self.tableCarne.setRowCount(len(rows))
            self.lblStatus.setText(f"Trabajadores con extra: {len(rows)}")

            for indice, dato in enumerate(rows):
                self.tableCarne.setItem(indice, 0, QTableWidgetItem(str(dato["nombre"])))
                self.tableCarne.setItem(indice, 1, QTableWidgetItem(str(dato["departamento"])))
                self.tableCarne.setItem(indice, 2, QTableWidgetItem(str(dato["total"])))
                self.tableCarne.setItem(indice, 3, QTableWidgetItem(str(dato["exceso"])))

        except Exception as e:
            QMessageBox.critical(self, "ERROR", f"No se pudo cargar la tabla: {e}")

    def generar_informe(self):
        try:
            file_path, _ = QFileDialog.getSaveFileName(self, "Guardar Informe", "informe_horas.pdf", "PDF Files (*.pdf)")
            if file_path:
                ReportService.generar_reporte(file_path)
                QMessageBox.information(self, "EXITO", "PDF Generado con éxito.")
        except Exception as e:
            QMessageBox.critical(self, "ERROR", f"Error PDF: {e}")