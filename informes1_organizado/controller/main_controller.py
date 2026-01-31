import os
from datetime import datetime
from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from views.main_window import MainWindow
from data.data_source import fetch_participants, compute_summary
from reports.report_service import build_participants_report

class MainController(MainWindow):
    def __init__(self, db_path, base_dir):
        super().__init__()
        # Importante: MainWindow ya llama a setupUi en su __init__ original
        self.db_path = db_path
        self.base_dir = base_dir

        # Conectar señales de la vista
        self.btn_refresh.clicked.connect(self.refresh_data)
        self.btn_export.clicked.connect(self.export_to_pdf)

        # Carga inicial
        self.refresh_data()

    def refresh_data(self):
        try:
            rows = fetch_participants(self.db_path)
            self.load_rows(rows)
            total, points_sum = compute_summary(rows)
            self.set_status(f"Participantes: {total} | Puntos: {points_sum}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudieron cargar los datos.\n\n{e}")

    def export_to_pdf(self):
        try:
            rows = fetch_participants(self.db_path)
            total, points_sum = compute_summary(rows)

            default_name = f"informe_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
            default_dir = os.path.join(self.base_dir, "reports", "output")
            os.makedirs(default_dir, exist_ok=True)

            path, _ = QFileDialog.getSaveFileName(
                self, "Guardar informe PDF",
                os.path.join(default_dir, default_name), "PDF (*.pdf)"
            )
            
            if path:
                build_participants_report(
                    output_path=path,
                    rows=rows,
                    summary=(total, points_sum),
                    title="Informe de participantes"
                )
                QMessageBox.information(self, "Éxito", f"PDF generado en:\n{path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo generar el PDF.\n\n{e}")