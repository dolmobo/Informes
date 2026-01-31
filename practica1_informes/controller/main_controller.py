import os
from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt
from views.main_window_ui import Ui_MainWindow
from data.data_source import fetch_participants, compute_summary

class MainController(QMainWindow, Ui_MainWindow):
    def __init__(self, db_path):
        super().__init__()
        self.setupUi(self)

        self.db_path = db_path

        self.btnRefresh.clicked.connect(self.cargar_datos)
        self.btnExport.clicked.connect(self.generar_informe)

        self.cargar_datos()

    def cargar_datos(self):
        try:
            rows = fetch_participants(self.db_path)

            self.tableWidget.setRowCount(len(rows))

            for i, r in enumerate(rows):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(str(r["name"])))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(str(r["department"])))
                
                item_puntos = QTableWidgetItem(str(r["points"]))
                self.tableWidget.setItem(i, 2, item_puntos)
            
            total, points_sum = compute_summary(rows)
            self.lblStatus.setText(f"Participantes: {total} | Puntos: {points_sum}")
        except Exception as e:
            QMessageBox.critical(self,"ERROR", "No se pudo cargar la informacion")

    def generar_informe(self):
        try:
            rows = fetch_participants(self.db_path)
            summary = compute_summary(rows)

            path, _ = QFileDialog.getSaveFileName(self, 
              "Exportar Informe PDF", 
              "informe_participantes.pdf",
              "Archivos PDF (*.pdf)"
            )

            if path:
                from reports.report_service import build_participants_report
                build_participants_report(path, rows, summary)

                QMessageBox.information(self, "Exito", "Informe generado.")
        except Exception as e:
            QMessageBox.critical(self, "ERROR:" ,"No se pudo crear al pdf")

