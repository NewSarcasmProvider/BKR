# File students.py

import openpyxl
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from data.data import DatabaseManager
from forms.confirmdeletedialog import ConfirmDeleteDialog
from import_export.import_manager import ImportManager
from import_export.export_manager import ExportManager

database = DatabaseManager()
import_manager = ImportManager()
export_manager = ExportManager()

class Ui_students(QtWidgets.QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setupUi(self)

    def setupUi(self, students):
        students.setObjectName("students")
        students.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(students)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.students_back = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.students_back.sizePolicy().hasHeightForWidth())
        self.students_back.setSizePolicy(sizePolicy)
        self.students_back.setMinimumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.students_back.setFont(font)
        self.students_back.setObjectName("students_back")
        self.verticalLayout.addWidget(self.students_back)
        self.upper_group = QtWidgets.QHBoxLayout()
        self.upper_group.setObjectName("upper_group")
        self.students_button_import = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.students_button_import.sizePolicy().hasHeightForWidth())
        self.students_button_import.setSizePolicy(sizePolicy)
        self.students_button_import.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.students_button_import.setFont(font)
        self.students_button_import.setObjectName("students_button_import")
        self.upper_group.addWidget(self.students_button_import)
        self.students_button_export = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.students_button_export.sizePolicy().hasHeightForWidth())
        self.students_button_export.setSizePolicy(sizePolicy)
        self.students_button_export.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.students_button_export.setFont(font)
        self.students_button_export.setObjectName("students_button_export")
        self.upper_group.addWidget(self.students_button_export)
        self.verticalLayout.addLayout(self.upper_group)
        self.lower_group = QtWidgets.QHBoxLayout()
        self.lower_group.setObjectName("lower_group")
        self.students_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.students_comboBox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.students_comboBox.setFont(font)
        self.students_comboBox.setObjectName("students_comboBox")
        self.lower_group.addWidget(self.students_comboBox)
        self.students_button_add = QtWidgets.QPushButton(self.centralwidget)
        self.students_button_add.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.students_button_add.setFont(font)
        self.students_button_add.setObjectName("students_button_add")
        self.lower_group.addWidget(self.students_button_add)
        self.students_button_delete = QtWidgets.QPushButton(self.centralwidget)
        self.students_button_delete.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.students_button_delete.setFont(font)
        self.students_button_delete.setObjectName("students_button_delete")
        self.lower_group.addWidget(self.students_button_delete)
        self.verticalLayout.addLayout(self.lower_group)
        self.students_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.students_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.students_lineEdit.setFont(font)
        self.students_lineEdit.setObjectName("students_lineEdit")
        self.verticalLayout.addWidget(self.students_lineEdit)
        self.students_tableView = QtWidgets.QTableView(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.students_tableView.setFont(font)
        self.students_tableView.setObjectName("students_tableView")
        self.verticalLayout.addWidget(self.students_tableView)
        students.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(students)
        self.statusbar.setObjectName("statusbar")
        students.setStatusBar(self.statusbar)

        self.retranslateUi(students)
        QtCore.QMetaObject.connectSlotsByName(students)


        self.students_comboBox.currentIndexChanged.connect(self.load_data_to_table)

        self.students_button_add.clicked.connect(self.add_students)
        self.students_button_delete.clicked.connect(self.delete_students)
        self.students_back.clicked.connect(self.go_back_to_main)
        self.students_button_import.clicked.connect(self.import_students)
        self.students_button_export.clicked.connect(self.export_students)

    def showEvent(self, event):
        super().showEvent(event)
        self.load_data_to_combobox()
        self.load_data_to_table()
    
    def retranslateUi(self, student):
        _translate = QtCore.QCoreApplication.translate
        student.setWindowTitle(_translate("student", "MainWindow"))
        self.students_back.setText(_translate("student", "Назад"))
        self.students_button_import.setText(_translate("student", "Импорт"))
        self.students_button_export.setText(_translate("student", "Экспорт"))
        self.students_button_add.setText(_translate("student", "Добавить ученика"))
        self.students_button_delete.setText(_translate("student", "Удалить ученика"))

    def go_back_to_main(self):
        self.close()
        self.main_window.show()

    def load_data_to_combobox(self):
        self.students_comboBox.clear()
        groups = database.get_groups()
        sorted_groups = sorted(groups, key=lambda x: x[1])
        for group in sorted_groups:
            self.students_comboBox.addItem(str(group[1]))

    def add_students(self):
        num_group = self.students_comboBox.currentText()
        students = self.students_lineEdit.text()
        database.create_students(num_group, students)
        self.load_data_to_table() 

    def delete_students(self):
        selected_index = self.students_tableView.selectedIndexes()
        if selected_index:
            selected_row = selected_index[0].row()
            student_name = self.students_tableView.model().index(selected_row, 2).data()

            confirm_dialog = ConfirmDeleteDialog(student_name)
            if confirm_dialog.exec_() == QtWidgets.QDialog.Accepted:
                num_group = self.students_tableView.model().index(selected_row, 1).data()

                database.delete_students(num_group, student_name)
                self.load_data_to_table()
        else:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Выберите дисциплину для удаления.")

    def load_data_to_table(self):
        num_group = self.students_comboBox.currentText()
        students_data = database.get_students_by_num_group(num_group)

        model = QtGui.QStandardItemModel(len(students_data), 3)
                
        model.setHorizontalHeaderLabels(['ID', 'NUM_GROUP', 'NAME'])

        for row, students in enumerate(students_data):
            for column, data in enumerate(students):
                item = QtGui.QStandardItem(str(data))
                model.setItem(row, column, item)

        self.students_tableView.setModel(model)

    def import_students(self):
        import_manager.import_data('students')
        self.load_data_to_combobox()
        self.load_data_to_table()

    
    def export_students(self):
        export_manager.export_data('students')
        self.load_data_to_combobox()
        self.load_data_to_table()