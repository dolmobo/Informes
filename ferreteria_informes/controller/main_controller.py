from PySide6.QtWidgets import QMainWindow, QMessageBox,QTableWidgetItem, QFileDialog
from views.MainWindow_ui import Ui_MainWindow

from data.data_source import DataSource

from service.report_generator import ReportService

class MainController(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        DataSource.ensure_db()
        self.cargar_tabla()

        self.btnRefrescar.clicked.connect(self.cargar_tabla)
        self.btnPDF.clicked.connect(self.generar_informe)
    
    def generar_informe(self):
        try:
            db_path, _ = QFileDialog().getSaveFileName(self, "Guardando informe de ferreteria.", "ferreteria.pdf", "PDF Files (*.pdf)")
            if db_path:
                ReportService.reporte_ferreteria(db_path)
                QMessageBox.information(self, "EXITO", "PDF Generado con exito.")
        except Exception as e:
            QMessageBox.critical(self, "ERROR", f"No se ha podido generar el pdf: {e}")

    def cargar_tabla(self):
        try:
            rows = DataSource.obtener_repuestos()
            total, suma_precio = DataSource.suma_precio(rows)
            
            self.tableCarne.setRowCount(len(rows))

            self.lblStatus.setText(f"Repuestos totales: {total} | Precio total: {suma_precio}")

            for indice, dato in enumerate(rows):
                self.tableCarne.setItem(indice, 0, QTableWidgetItem(str(dato["repuesto"])))
                self.tableCarne.setItem(indice, 1, QTableWidgetItem(str(dato["descripcion"])))
                self.tableCarne.setItem(indice, 2, QTableWidgetItem(str(dato["precio"])))

        except Exception as e:
            QMessageBox.critical(self, "ERROR", f"No se pudo cargar la tabla: {e}")

            