from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QSizePolicy,
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Reports App - Participantes")
        self.resize(850, 520)

        root = QWidget()
        self.setCentralWidget(root)
        layout = QVBoxLayout(root)

        header = QLabel("Participantes (SQLite) → Informe PDF (ReportLab)")
        header.setStyleSheet("font-size: 16px; font-weight: 600;")
        layout.addWidget(header)

        # Actions
        actions = QHBoxLayout()
        self.btn_refresh = QPushButton("Recargar datos")
        self.btn_export = QPushButton("Exportar PDF…")
        self.status = QLabel("Listo")
        self.status.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.status.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        actions.addWidget(self.btn_refresh)
        actions.addWidget(self.btn_export)
        actions.addWidget(self.status)
        layout.addLayout(actions)

        # Table
        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["Nombre", "Departamento", "Puntos"])
        self.table.setAlternatingRowColors(True)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)
        self.table.horizontalHeader().setStretchLastSection(False)
        self.table.horizontalHeader().setDefaultAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.table.setColumnWidth(0, 360)
        self.table.setColumnWidth(1, 260)
        self.table.setColumnWidth(2, 120)
        layout.addWidget(self.table)

    def set_status(self, text: str) -> None:
        self.status.setText(text)

    def load_rows(self, rows: list[dict]) -> None:
        self.table.setRowCount(len(rows))
        for i, r in enumerate(rows):
            name_item = QTableWidgetItem(str(r["name"]))
            dept_item = QTableWidgetItem(str(r["department"]))
            points_item = QTableWidgetItem(str(int(r["points"])))

            # Align numeric right
            points_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

            self.table.setItem(i, 0, name_item)
            self.table.setItem(i, 1, dept_item)
            self.table.setItem(i, 2, points_item)

        self.table.resizeRowsToContents()
