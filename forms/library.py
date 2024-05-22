# File library.py

from PyQt5 import QtCore, QtGui, QtWidgets
from data.data import DatabaseManager
from import_export.export_manager import ExportManager

database = DatabaseManager()
export_manager = ExportManager()

class Ui_library(QtWidgets.QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setupUi(self)

    def setupUi(self, library):
        library.setObjectName("library")
        library.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(library)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.library_back = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.library_back.sizePolicy().hasHeightForWidth())
        self.library_back.setSizePolicy(sizePolicy)
        self.library_back.setMinimumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.library_back.setFont(font)
        self.library_back.setObjectName("library_back")
        self.verticalLayout.addWidget(self.library_back)
        self.group = QtWidgets.QHBoxLayout()
        self.group.setObjectName("group")
        self.library_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.library_comboBox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.library_comboBox.setFont(font)
        self.library_comboBox.setObjectName("library_comboBox")
        self.group.addWidget(self.library_comboBox)
        self.library_button_statistics = QtWidgets.QPushButton(self.centralwidget)
        self.library_button_statistics.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.library_button_statistics.setFont(font)
        self.library_button_statistics.setObjectName("library_button_statistics")
        self.group.addWidget(self.library_button_statistics)
        self.library_button_export = QtWidgets.QPushButton(self.centralwidget)
        self.library_button_export.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.library_button_export.setFont(font)
        self.library_button_export.setObjectName("library_button_export")
        self.group.addWidget(self.library_button_export)
        self.verticalLayout.addLayout(self.group)
        self.library_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.library_tableWidget.setFont(font)
        self.library_tableWidget.setObjectName("library_tableWidget")
        self.library_tableWidget.setColumnCount(0)
        self.library_tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.library_tableWidget)
        library.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(library)
        self.statusbar.setObjectName("statusbar")
        library.setStatusBar(self.statusbar)

        self.retranslateUi(library)
        QtCore.QMetaObject.connectSlotsByName(library)

        self.load_data_to_combobox()
        self.load_data_to_table()

        self.library_comboBox.currentIndexChanged.connect(self.load_data_to_table)

        self.library_back.clicked.connect(self.go_back_to_main)
        self.library_button_statistics.clicked.connect(self.go_statistics)
        self.library_button_statistics.clicked.connect(self.main_window.open_statistics_window)

        self.library_button_export.clicked.connect(self.export_library)

    def retranslateUi(self, library):
        _translate = QtCore.QCoreApplication.translate
        library.setWindowTitle(_translate("library", "MainWindow"))
        self.library_back.setText(_translate("library", "Назад"))
        self.library_button_statistics.setText(_translate("library", "Статистика"))
        self.library_button_export.setText(_translate("library", "Экспорт"))

    def go_back_to_main(self):
        self.close()
        self.main_window.show()

    def go_statistics(self):
        self.close()
    
    def load_data_to_combobox(self):
        self.library_comboBox.clear()
        groups = database.get_groups()
        sorted_groups = sorted(groups, key=lambda x: x[1])
        for group in sorted_groups:
            self.library_comboBox.addItem(str(group[1]))

    def load_data_to_table(self):
        self.library_tableWidget.clear()

        num_group = self.library_comboBox.currentText()
        disciplines_data = database.get_disciplines_by_num_group(num_group)
        name_disciplines_data = [row[2] for row in disciplines_data]

        self.library_tableWidget.setColumnCount(len(name_disciplines_data))
        self.library_tableWidget.setHorizontalHeaderLabels(name_disciplines_data)

        students_data = database.get_students_by_num_group(num_group)
        name_students_data = [row[2] for row in students_data]

        self.library_tableWidget.setRowCount(len(name_students_data))
        self.library_tableWidget.setVerticalHeaderLabels(name_students_data)

        for row in range(len(name_students_data)):
            for col in range(len(name_disciplines_data)):
                combo_box = QtWidgets.QComboBox()
                books_data = database.get_books_by_num_group_and_disciplines(num_group, name_disciplines_data[col])
                combo_box.addItem("не выдана")
                for book_data in books_data:
                    combo_box.addItem(str(book_data[3]))

                current_value = database.get_library_value(num_group, name_students_data[row], name_disciplines_data[col])
                if current_value is None:
                    self.update_database_value(num_group, name_students_data[row], name_disciplines_data[col], "не выдана")
                    index = 0
                else:
                    index = combo_box.findText(current_value)

                combo_box.setCurrentIndex(index)
                self.library_tableWidget.setCellWidget(row, col, combo_box)


                combo_box.currentIndexChanged.connect(lambda index, num_group=num_group, student=name_students_data[row], discipline=name_disciplines_data[col], combo_box=combo_box: self.update_database_value(num_group, student, discipline, combo_box.currentText()))

    def update_database_value(self, num_group, student, discipline, value):
        database.update_database_value(num_group, student, discipline, value)

    def export_library(self):
        num_group = self.library_comboBox.currentText()
        export_manager.export_data('library', num_group)
        self.load_data_to_table()