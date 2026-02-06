from PySide6.QtWidgets import QApplication
from controller.main_controller import MainController
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = MainController()
    ventana.show()

    sys.exit(app.exec())