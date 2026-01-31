import sys
import os
from PySide6.QtWidgets import QApplication
from controller.main_controller import MainController
from data.data_source import get_db_path, ensure_db

def main():
    app = QApplication(sys.argv)
    
    # Configuración de rutas y base de datos
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = get_db_path(base_dir)
    ensure_db(db_path)

    # Iniciar el controlador principal
    ventana = MainController(db_path, base_dir)
    ventana.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()