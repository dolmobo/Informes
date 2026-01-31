# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
        MainWindow.resize(1186, 602)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 10, 1151, 531))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lblTituloPla = QLabel(self.widget)
        self.lblTituloPla.setObjectName(u"lblTituloPla")

        self.verticalLayout_2.addWidget(self.lblTituloPla)

        self.playerTable = QTableWidget(self.widget)
        if (self.playerTable.columnCount() < 3):
            self.playerTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.playerTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.playerTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.playerTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.playerTable.setObjectName(u"playerTable")

        self.verticalLayout_2.addWidget(self.playerTable)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnRefreshPla = QPushButton(self.widget)
        self.btnRefreshPla.setObjectName(u"btnRefreshPla")

        self.horizontalLayout_2.addWidget(self.btnRefreshPla)

        self.btnExportPla = QPushButton(self.widget)
        self.btnExportPla.setObjectName(u"btnExportPla")

        self.horizontalLayout_2.addWidget(self.btnExportPla)

        self.lblStatusPla = QLabel(self.widget)
        self.lblStatusPla.setObjectName(u"lblStatusPla")

        self.horizontalLayout_2.addWidget(self.lblStatusPla)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitulo = QLabel(self.widget)
        self.lblTitulo.setObjectName(u"lblTitulo")

        self.verticalLayout.addWidget(self.lblTitulo)

        self.tableWidget = QTableWidget(self.widget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnRefresh = QPushButton(self.widget)
        self.btnRefresh.setObjectName(u"btnRefresh")

        self.horizontalLayout.addWidget(self.btnRefresh)

        self.btnExport = QPushButton(self.widget)
        self.btnExport.setObjectName(u"btnExport")

        self.horizontalLayout.addWidget(self.btnExport)

        self.lblStatus = QLabel(self.widget)
        self.lblStatus.setObjectName(u"lblStatus")

        self.horizontalLayout.addWidget(self.lblStatus)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1186, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblTituloPla.setText(QCoreApplication.translate("MainWindow", u"GESTION DE JUGADORES", None))
        ___qtablewidgetitem = self.playerTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem1 = self.playerTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Equipo", None));
        ___qtablewidgetitem2 = self.playerTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Edad", None));
        self.btnRefreshPla.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
        self.btnExportPla.setText(QCoreApplication.translate("MainWindow", u"Exportar pdf", None))
        self.lblStatusPla.setText(QCoreApplication.translate("MainWindow", u"lblstatus", None))
        self.lblTitulo.setText(QCoreApplication.translate("MainWindow", u"GESTION DE PARTICIPANTES", None))
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Departamento", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Puntos", None));
        self.btnRefresh.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
        self.btnExport.setText(QCoreApplication.translate("MainWindow", u"Exportar pdf", None))
        self.lblStatus.setText(QCoreApplication.translate("MainWindow", u"lblstatus", None))
    # retranslateUi

