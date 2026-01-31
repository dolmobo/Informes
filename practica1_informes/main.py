import sys
import os
from controller.main_controller import MainController
from PySide6.QtWidgets import QApplication

from data.data_source import get_db_path, ensure_db

if __name__ == "__main__":
    app = QApplication(sys.argv)

    base_dir = os.path.dirname(os.path.abspath(__file__))

    db_path = get_db_path(base_dir)

    ensure_db(db_path)

    ventana = MainController(db_path)
    ventana.show()

    sys.exit(app.exec())