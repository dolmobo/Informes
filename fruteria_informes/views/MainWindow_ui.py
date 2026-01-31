# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 791, 541))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lblTitulo = QLabel(self.widget)
        self.lblTitulo.setObjectName(u"lblTitulo")

        self.verticalLayout.addWidget(self.lblTitulo)

        self.tableFruta = QTableWidget(self.widget)
        self.tableFruta.setObjectName(u"tableFruta")

        self.verticalLayout.addWidget(self.tableFruta)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnRefrescar = QPushButton(self.widget)
        self.btnRefrescar.setObjectName(u"btnRefrescar")

        self.horizontalLayout.addWidget(self.btnRefrescar)

        self.btnPDF = QPushButton(self.widget)
        self.btnPDF.setObjectName(u"btnPDF")

        self.horizontalLayout.addWidget(self.btnPDF)

        self.lblStatus = QLabel(self.widget)
        self.lblStatus.setObjectName(u"lblStatus")

        self.horizontalLayout.addWidget(self.lblStatus)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblTitulo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">GESTION DE FRUTERIA</span></p></body></html>", None))
        self.btnRefrescar.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
        self.btnPDF.setText(QCoreApplication.translate("MainWindow", u"Exportar PDF", None))
        self.lblStatus.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
    # retranslateUi

