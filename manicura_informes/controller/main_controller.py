from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QFileDialog
from views.MainWindow_ui import Ui_MainWindow

from data.data_source import DataSource
from service.report_manicura import ReportManicura

class MainController(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        DataSource.ensure_db()
        self.refrescar_tabla()

        self.btnRefrescar.clicked.connect(self.refrescar_tabla)
        self.btnPDF.clicked.connect(self.generar_pdf)

    def generar_pdf(self):
        try:
            db_path, _ = QFileDialog.getSaveFileName(self, "Guardar informe manicura", "manicura.pdf", "PDF Files (*.pdf)")
            
            if db_path:
                ReportManicura.reporte_manicura(db_path)
                QMessageBox.information(self,"EXITO", "PDF de manicura generado con exito")
        except Exception as e:
            QMessageBox.critical(self, "ERROR", f"No se ha podido generar el PDF: {e}")

    def refrescar_tabla(self):
        try:
            rows = DataSource.obtener_manicura()
            total, suma_precio = DataSource.suma_precios(rows)

            self.tableNails.setRowCount(len(rows))

            self.lblStatus.setText(f"Servicios totales: {total} | Precio total: {suma_precio}")

            for indice, dato in enumerate(rows):
                self.tableNails.setItem(indice, 0, QTableWidgetItem(str(dato["name"])))
                self.tableNails.setItem(indice, 1, QTableWidgetItem(str(dato["descripcion"])))
                self.tableNails.setItem(indice, 2, QTableWidgetItem(str(dato["precio"])))

        except Exception as e:
            QMessageBox.critical(self,"ERROR", f"No se pudo cargar la tabla : {e}")