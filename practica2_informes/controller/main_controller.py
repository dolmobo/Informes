from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QFileDialog
from PySide6.QtCore import Qt
from views.main_window_ui import Ui_MainWindow
from reports.report_service import ReportService

from data.data_source import DataSource

class MainController(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #ASEGURAR BASE DE DATOS
        DataSource.ensure_db()

        # Conectar botones

        self.btnRefresh.clicked.connect(self.cargar_participantes)
        self.btnExport.clicked.connect(self.exportar_participantes)

        self.btnRefreshPla.clicked.connect(self.cargar_jugadores)
        self.btnExportPla.clicked.connect(self.exportar_jugadores)

        self.cargar_participantes()
        self.cargar_jugadores()

    def cargar_participantes(self):
        try:
            #Obtenemos las filas (datos)
            rows = DataSource.obtener_participants()

            self.tableWidget.setRowCount(len(rows))

            for indice, data in enumerate(rows):
                self.tableWidget.setItem(indice, 0, QTableWidgetItem(str(data["name"])))
                self.tableWidget.setItem(indice, 1, QTableWidgetItem(str(data["department"])))
                self.tableWidget.setItem(indice, 2, QTableWidgetItem(str(data["points"])))
        
            total, suma_puntos = DataSource.suma_puntos(rows)
            self.lblStatus.setText(f"Participantes: {total} | Total puntos: {suma_puntos}")

        except Exception as e:
            print("Error cargando participantes")

    def exportar_participantes(self):
        try:
            file_path, _ = QFileDialog.getSaveFileName(
                self, "Guardar Informe Participantes", "participantes.pdf", "PDF Files (*.pdf)"
            )

            if file_path:
                ReportService.reporte_participantes(file_path)
                QMessageBox.information(self, "Exito", "PDF Generado con exito")
        except Exception:
            QMessageBox.warning(self, "ERROR" "No se ha podido generar el PDF")

    def cargar_jugadores(self):
        try:
            rows = DataSource.obtener_jugadores()
            self.playerTable.setRowCount(len(rows))

            for indice, data in enumerate (rows):
                self.playerTable.setItem(indice, 0, QTableWidgetItem(str(data["name"])))
                self.playerTable.setItem(indice, 1, QTableWidgetItem(str(data["team"])))
                self.playerTable.setItem(indice, 2, QTableWidgetItem(str(data["age"])))

            total, suma_edad = DataSource.suma_edad(rows)
            self.lblStatusPla.setText(f"Jugadores: {total} | Suma edad: {suma_edad}")

        except Exception:
            print("ERROR CARGANDO JUGADORES")

    def exportar_jugadores(self):
        try:
            file_path, _ = QFileDialog.getSaveFileName(
                self, "Guardar informe generado", "jugadores.pdf", "PDF Files (*.pdf)"
            )
            if file_path:
                ReportService.reporte_jugadores(file_path)
                QMessageBox.information(self, "EXITO","PDF Generado con exito")
        except Exception:
            QMessageBox.warning(self, "ERROR","No se ha podido generar el PDF")