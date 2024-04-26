from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_statistics(object):
    def setupUi(self, statistics):
        statistics.setObjectName("statistics")
        statistics.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(statistics)
        self.centralwidget.setObjectName("centralwidget")
        self.statistics_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.statistics_tableWidget.setGeometry(QtCore.QRect(20, 20, 760, 560))
        self.statistics_tableWidget.setObjectName("statistics_tableWidget")
        self.statistics_tableWidget.setColumnCount(0)
        self.statistics_tableWidget.setRowCount(0)
        statistics.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(statistics)
        self.statusbar.setObjectName("statusbar")
        statistics.setStatusBar(self.statusbar)

        self.retranslateUi(statistics)
        QtCore.QMetaObject.connectSlotsByName(statistics)

    def retranslateUi(self, statistics):
        _translate = QtCore.QCoreApplication.translate
        statistics.setWindowTitle(_translate("statistics", "MainWindow"))
