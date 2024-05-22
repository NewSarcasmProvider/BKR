from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from lib_statistics.statistics_manager import StatisticsManager

class Ui_statistics(QtWidgets.QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.statistics_manager = StatisticsManager()
        self.setupUi(self)

    def setupUi(self, statistics):
        statistics.setObjectName("statistics")
        statistics.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(statistics)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.statistics_back = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statistics_back.sizePolicy().hasHeightForWidth())
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.statistics_back.setSizePolicy(sizePolicy)
        self.statistics_back.setFont(font)
        self.statistics_back.setMinimumSize(QtCore.QSize(90, 30))
        self.statistics_back.setObjectName("statistics_back")
        self.verticalLayout.addWidget(self.statistics_back)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.statistics_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.statistics_comboBox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.statistics_comboBox.setFont(font)
        self.statistics_comboBox.setObjectName("statistics_comboBox")
        self.horizontalLayout.addWidget(self.statistics_comboBox)
        self.students_statistics = QtWidgets.QPushButton(self.centralwidget)
        self.students_statistics.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.students_statistics.setFont(font)
        self.students_statistics.setObjectName("students_statistics")
        self.horizontalLayout.addWidget(self.students_statistics)
        self.groups_statistics = QtWidgets.QPushButton(self.centralwidget)
        self.groups_statistics.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.groups_statistics.setFont(font)
        self.groups_statistics.setObjectName("groups_statistics")
        self.horizontalLayout.addWidget(self.groups_statistics)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.statistics_tableView = QtWidgets.QTableView(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.statistics_tableView.setFont(font)
        self.statistics_tableView.setObjectName("statistics_tableView")
        self.verticalLayout.addWidget(self.statistics_tableView)
        statistics.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(statistics)
        self.statusbar.setObjectName("statusbar")
        statistics.setStatusBar(self.statusbar)

        self.retranslateUi(statistics)
        QtCore.QMetaObject.connectSlotsByName(statistics)

        self.statistics_back.clicked.connect(self.go_back_to_main)
        self.statistics_back.clicked.connect(self.main_window.open_library_window)
        self.students_statistics.clicked.connect(lambda: self.load_data_to_table("students"))
        self.groups_statistics.clicked.connect(lambda: self.load_data_to_table("groups"))

    def showEvent(self, event):
        super().showEvent(event)
        self.load_data_to_combobox()
        self.load_data_to_table()

    def retranslateUi(self, statistics):
        _translate = QtCore.QCoreApplication.translate
        statistics.setWindowTitle(_translate("statistics", "Статистика"))
        self.statistics_back.setText(_translate("statistics", "Назад"))
        self.students_statistics.setText(_translate("statistics", "Статистика по студентам"))
        self.groups_statistics.setText(_translate("statistics", "Статистика по группам"))

    def go_back_to_main(self):
        self.close()

    def load_data_to_combobox(self):
        self.statistics_comboBox.clear()
        groups = self.statistics_manager.database.get_groups()
        sorted_groups = sorted(groups, key=lambda x: x[1])
        for group in sorted_groups:
            self.statistics_comboBox.addItem(str(group[1]))

    def load_data_to_table(self, stat_type="students"):
        model = QStandardItemModel()
        if stat_type == "students":
            self.load_student_statistics(model)
        elif stat_type == "groups":
            self.load_group_statistics(model)
        self.statistics_tableView.setModel(model)
        self.statistics_tableView.resizeColumnsToContents()

    def load_student_statistics(self, model):
        group_num = self.statistics_comboBox.currentText()
        student_statistics = self.statistics_manager.calculate_student_statistics(group_num)
        
        model.setHorizontalHeaderLabels(["Студент", "Процент выданных книг"])
        for student_name, percentage in student_statistics:
            model.appendRow([QStandardItem(student_name), QStandardItem(f"{percentage:.2f}%")])

    def load_group_statistics(self, model):
        group_statistics = self.statistics_manager.calculate_group_statistics()
        
        model.setHorizontalHeaderLabels(["Группа", "Процент выданных книг"])
        for group_num, percentage in group_statistics:
            model.appendRow([QStandardItem(str(group_num)), QStandardItem(f"{percentage:.2f}%")])
