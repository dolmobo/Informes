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
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 791, 541))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lblTitulo = QLabel(self.layoutWidget)
        self.lblTitulo.setObjectName(u"lblTitulo")

        self.verticalLayout.addWidget(self.lblTitulo)

        self.tableCarne = QTableWidget(self.layoutWidget)
        if (self.tableCarne.columnCount() < 3):
            self.tableCarne.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableCarne.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableCarne.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableCarne.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableCarne.setObjectName(u"tableCarne")

        self.verticalLayout.addWidget(self.tableCarne)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnRefrescar = QPushButton(self.layoutWidget)
        self.btnRefrescar.setObjectName(u"btnRefrescar")

        self.horizontalLayout.addWidget(self.btnRefrescar)

        self.btnPDF = QPushButton(self.layoutWidget)
        self.btnPDF.setObjectName(u"btnPDF")

        self.horizontalLayout.addWidget(self.btnPDF)

        self.lblStatus = QLabel(self.layoutWidget)
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
        self.lblTitulo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">GESTION DE CARNICERIA</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableCarne.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nueva columna", None));
        ___qtablewidgetitem1 = self.tableCarne.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem2 = self.tableCarne.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Peso (KG)", None));
        self.btnRefrescar.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
        self.btnPDF.setText(QCoreApplication.translate("MainWindow", u"Exportar PDF", None))
        self.lblStatus.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
    # retranslateUi

