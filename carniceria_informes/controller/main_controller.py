from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QFileDialog
from views.MainWindow_ui import Ui_MainWindow

from service.report_generator import ReportService
from data.data_source import DataSource

class MainController(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        DataSource.ensure_db()

        self.cargar_tabla()

        self.btnRefrescar.clicked.connect(self.cargar_tabla)
        self.btnPDF.clicked.connect(self.generar_pdf)

    def generar_pdf(self):
         try:
              db_path, _ = QFileDialog.getSaveFileName(self, "Guardar informe carniceria", "carniceria.pdf", "PDF Files (*.pdf)")
              if db_path:
                   ReportService.reporte_carniceria(db_path)
                   QMessageBox.information(self, "EXITO", "PDF generado con exito.")
         except Exception:
                   QMessageBox.critical(self, "ERROR", "No ha sido posible generar el pdf.")
             

    def cargar_tabla(self):
         try:
              rows = DataSource.obtener_carnes()
              total, suma_kg = DataSource.suma_kg(rows)

              self.tableCarne.setRowCount(len(rows))

              self.lblStatus.setText(f"Total carnes: {total} | Peso total: {suma_kg}")

              for indice, dato in enumerate(rows):
                   self.tableCarne.setItem(indice, 0, QTableWidgetItem(str(dato["carne"])))
                   self.tableCarne.setItem(indice, 1, QTableWidgetItem(str(dato["tipo"])))
                   self.tableCarne.setItem(indice, 2, QTableWidgetItem(str(dato["peso"])))

         except Exception as e:
              QMessageBox.critical(self, "ERROR", f"No se ha podido cargar la talba. {e}")