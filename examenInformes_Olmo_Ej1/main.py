import sys
from controller.main_controller import MainController
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = MainController()
    ventana.show()

    sys.exit(app.exec())