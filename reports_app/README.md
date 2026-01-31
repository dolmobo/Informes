# reports_app

App PySide6 que lee participantes desde SQLite y genera un informe PDF con ReportLab (Platypus).

## Requisitos
- Python 3.10+
- PySide6
- reportlab

## Instalar
```bash
pip install -r requirements.txt
```

## Ejecutar
```bash
python main.py
```

La BD se crea/llena automáticamente en `data/database.db` si está vacía.
Los PDFs se guardan por defecto en `reports/output/`.
