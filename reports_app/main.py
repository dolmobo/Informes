import os
import sys
from datetime import datetime

from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox

from ui.main_window import MainWindow
from data.data_source import get_db_path, ensure_db, fetch_participants, compute_summary
from reports.report_generator import build_participants_report


def main() -> int:
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Ensure DB exists (and seed if empty)
    db_path = get_db_path(base_dir)
    ensure_db(db_path)

    app = QApplication(sys.argv)
    window = MainWindow()

    def refresh() -> None:
        try:
            rows = fetch_participants(db_path)
            window.load_rows(rows)
            total, points_sum = compute_summary(rows)
            window.set_status(f"Participantes: {total} | Puntos: {points_sum}")
        except Exception as e:
            QMessageBox.critical(window, "Error", f"No se pudieron cargar los datos.\n\n{e}")

    def export_pdf() -> None:
        try:
            rows = fetch_participants(db_path)
            total, points_sum = compute_summary(rows)

            default_name = f"informe_participantes_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
            default_dir = os.path.join(base_dir, "reports", "output")
            os.makedirs(default_dir, exist_ok=True)

            path, _ = QFileDialog.getSaveFileName(
                window,
                "Guardar informe PDF",
                os.path.join(default_dir, default_name),
                "PDF (*.pdf)",
            )
            if not path:
                return

            build_participants_report(
                output_path=path,
                rows=rows,
                summary=(total, points_sum),
                title="Informe de participantes",
            )

            QMessageBox.information(window, "PDF generado", f"Informe creado:\n{path}")
            window.set_status(f"PDF generado: {os.path.basename(path)}")
        except Exception as e:
            QMessageBox.critical(window, "Error", f"No se pudo generar el PDF.\n\n{e}")

    window.btn_refresh.clicked.connect(refresh)
    window.btn_export.clicked.connect(export_pdf)

    refresh()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
