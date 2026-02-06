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
        MainWindow.resize(1604, 607)
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

        self.tableEmpleados = QTableWidget(self.layoutWidget)
        if (self.tableEmpleados.columnCount() < 4):
            self.tableEmpleados.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableEmpleados.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableEmpleados.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableEmpleados.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableEmpleados.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableEmpleados.setObjectName(u"tableEmpleados")

        self.verticalLayout.addWidget(self.tableEmpleados)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnRefrescarEmpleados = QPushButton(self.layoutWidget)
        self.btnRefrescarEmpleados.setObjectName(u"btnRefrescarEmpleados")

        self.horizontalLayout.addWidget(self.btnRefrescarEmpleados)

        self.btnPDFEmpleados = QPushButton(self.layoutWidget)
        self.btnPDFEmpleados.setObjectName(u"btnPDFEmpleados")

        self.horizontalLayout.addWidget(self.btnPDFEmpleados)

        self.lblStatusEmpleados = QLabel(self.layoutWidget)
        self.lblStatusEmpleados.setObjectName(u"lblStatusEmpleados")

        self.horizontalLayout.addWidget(self.lblStatusEmpleados)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.layoutWidget_2 = QWidget(self.centralwidget)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(790, 0, 791, 541))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lblTitulo_2 = QLabel(self.layoutWidget_2)
        self.lblTitulo_2.setObjectName(u"lblTitulo_2")

        self.verticalLayout_2.addWidget(self.lblTitulo_2)

        self.table_jornadas = QTableWidget(self.layoutWidget_2)
        if (self.table_jornadas.columnCount() < 4):
            self.table_jornadas.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_jornadas.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_jornadas.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_jornadas.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_jornadas.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.table_jornadas.setObjectName(u"table_jornadas")

        self.verticalLayout_2.addWidget(self.table_jornadas)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnRefrescarJornada = QPushButton(self.layoutWidget_2)
        self.btnRefrescarJornada.setObjectName(u"btnRefrescarJornada")

        self.horizontalLayout_2.addWidget(self.btnRefrescarJornada)

        self.btnPDF_Jornada = QPushButton(self.layoutWidget_2)
        self.btnPDF_Jornada.setObjectName(u"btnPDF_Jornada")

        self.horizontalLayout_2.addWidget(self.btnPDF_Jornada)

        self.lblStatus_Jornada = QLabel(self.layoutWidget_2)
        self.lblStatus_Jornada.setObjectName(u"lblStatus_Jornada")

        self.horizontalLayout_2.addWidget(self.lblStatus_Jornada)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1604, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblTitulo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">GESTION DE EMPLEADOS</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableEmpleados.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem1 = self.tableEmpleados.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Departamento", None));
        ___qtablewidgetitem2 = self.tableEmpleados.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Total (h)", None));
        ___qtablewidgetitem3 = self.tableEmpleados.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Exceso (h)", None));
        self.btnRefrescarEmpleados.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
        self.btnPDFEmpleados.setText(QCoreApplication.translate("MainWindow", u"Exportar PDF", None))
        self.lblStatusEmpleados.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
        self.lblTitulo_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">GESTION DE JORNADA</span></p></body></html>", None))
        ___qtablewidgetitem4 = self.table_jornadas.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem5 = self.table_jornadas.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Departamento", None));
        ___qtablewidgetitem6 = self.table_jornadas.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem7 = self.table_jornadas.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Horas", None));
        self.btnRefrescarJornada.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
        self.btnPDF_Jornada.setText(QCoreApplication.translate("MainWindow", u"Exportar PDF", None))
        self.lblStatus_Jornada.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
    # retranslateUi

