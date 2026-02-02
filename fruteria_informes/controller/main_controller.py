from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QFileDialog
from views.MainWindow_ui import Ui_MainWindow
from data.data_source import DataSource

from service.report_generator import ReportService

class MainController(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        DataSource.const_bd()

        self.btnRefrescar.clicked.connect(self.refrescar_tabla)
        self.btnPDF.clicked.connect(self.generar_pdf)

        self.refrescar_tabla()

    def refrescar_tabla(self):
        try:
            rows = DataSource.obtener_frutas()

            self.tableFruta.setRowCount(len(rows))

            for indice, dato in enumerate(rows):
                self.tableFruta.setItem(indice, 0, QTableWidgetItem(str(dato["nombre"])))
                self.tableFruta.setItem(indice, 1, QTableWidgetItem(str(dato["tipo"])))
                self.tableFruta.setItem(indice, 2, QTableWidgetItem(str(dato["peso"])))

            total, suma_peso = DataSource.suma_peso(rows)
            self.lblStatus.setText(f"Frutas: {total} | Peso total: {suma_peso}")

        except Exception as e:
            QMessageBox.critical(self,"ERROR", f"No se ha podido cargar la tabla. {e}")

    def generar_pdf(self):
        try:
            file_path, _ = QFileDialog.getSaveFileName(
                self, "Guardar informe fruteria", "fruteria_informe.pdf", "PDF Files (*.pdf)"
            )

            if file_path:
                ReportService.reporte_fruteria(file_path)
                QMessageBox.information(self, "EXITO", "PDF Generado con exito")
        except Exception:
            QMessageBox.critical(self, "EXITO", "NO SE HA PODIDO GENERAR EL PDF")
            