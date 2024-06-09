# File disciplines.py

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

class Ui_disciplines(QtWidgets.QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setupUi(self)

    def setupUi(self, disciplines):
        disciplines.setObjectName("disciplines")
        disciplines.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(disciplines)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.disciplines_back = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disciplines_back.sizePolicy().hasHeightForWidth())
        self.disciplines_back.setSizePolicy(sizePolicy)
        self.disciplines_back.setMinimumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.disciplines_back.setFont(font)
        self.disciplines_back.setObjectName("disciplines_back")
        self.verticalLayout.addWidget(self.disciplines_back)
        self.upper_group = QtWidgets.QHBoxLayout()
        self.upper_group.setObjectName("upper_group")
        self.disciplines_button_import = QtWidgets.QPushButton(self.centralwidget)
        self.disciplines_button_import.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.disciplines_button_import.setFont(font)
        self.disciplines_button_import.setObjectName("disciplines_button_import")
        self.upper_group.addWidget(self.disciplines_button_import)
        self.disciplines_button_export = QtWidgets.QPushButton(self.centralwidget)
        self.disciplines_button_export.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.disciplines_button_export.setFont(font)
        self.disciplines_button_export.setObjectName("disciplines_button_export")
        self.upper_group.addWidget(self.disciplines_button_export)
        self.verticalLayout.addLayout(self.upper_group)
        self.lower_group = QtWidgets.QHBoxLayout()
        self.lower_group.setObjectName("lower_group")
        self.disciplines_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.disciplines_comboBox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.disciplines_comboBox.setFont(font)
        self.disciplines_comboBox.setObjectName("disciplines_comboBox")
        self.lower_group.addWidget(self.disciplines_comboBox)
        self.disciplines_button_add = QtWidgets.QPushButton(self.centralwidget)
        self.disciplines_button_add.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.disciplines_button_add.setFont(font)
        self.disciplines_button_add.setObjectName("disciplines_button_add")
        self.lower_group.addWidget(self.disciplines_button_add)
        self.disciplines_button_delete = QtWidgets.QPushButton(self.centralwidget)
        self.disciplines_button_delete.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.disciplines_button_delete.setFont(font)
        self.disciplines_button_delete.setObjectName("disciplines_button_delete")
        self.lower_group.addWidget(self.disciplines_button_delete)
        self.verticalLayout.addLayout(self.lower_group)
        self.disciplines_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.disciplines_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.disciplines_lineEdit.setFont(font)
        self.disciplines_lineEdit.setObjectName("disciplines_lineEdit")
        self.verticalLayout.addWidget(self.disciplines_lineEdit)
        self.disciplines_tableView = QtWidgets.QTableView(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.disciplines_tableView.setFont(font)
        self.disciplines_tableView.setObjectName("disciplines_tableView")
        self.verticalLayout.addWidget(self.disciplines_tableView)
        disciplines.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(disciplines)
        self.statusbar.setObjectName("statusbar")
        disciplines.setStatusBar(self.statusbar)

        self.retranslateUi(disciplines)
        QtCore.QMetaObject.connectSlotsByName(disciplines)

        self.disciplines_comboBox.currentIndexChanged.connect(self.load_data_to_table)

        self.disciplines_button_add.clicked.connect(self.add_disciplines)
        self.disciplines_button_delete.clicked.connect(self.delete_disciplines)
        self.disciplines_back.clicked.connect(self.go_back_to_main)
        self.disciplines_button_import.clicked.connect(self.import_disciplines)
        self.disciplines_button_export.clicked.connect(self.export_disciplines)

    def showEvent(self, event):
        super().showEvent(event)
        self.load_data_to_combobox()
        self.load_data_to_table()
    
    def retranslateUi(self, disciplines):
        _translate = QtCore.QCoreApplication.translate
        disciplines.setWindowTitle(_translate("disciplines", "MainWindow"))
        self.disciplines_back.setText(_translate("disciplines", "Назад"))
        self.disciplines_button_import.setText(_translate("disciplines", "Импорт"))
        self.disciplines_button_export.setText(_translate("disciplines", "Экспорт"))
        self.disciplines_button_add.setText(_translate("disciplines", "Добавить предмет"))
        self.disciplines_button_delete.setText(_translate("disciplines", "Удалить предмет"))

    def go_back_to_main(self):
        self.close() 
        self.main_window.show()
    
    def load_data_to_combobox(self):
        self.disciplines_comboBox.clear()
        groups = database.get_groups()
        sorted_groups = sorted(groups, key=lambda x: x[1])
        for group in sorted_groups:
            self.disciplines_comboBox.addItem(str(group[1]))


    def add_disciplines(self):
        num_group = self.disciplines_comboBox.currentText()
        disciplines = self.disciplines_lineEdit.text()
        database.create_disciplines(num_group, disciplines)
        self.load_data_to_table() 

    def delete_disciplines(self):
        selected_index = self.disciplines_tableView.selectedIndexes()
        if selected_index:
            selected_row = selected_index[0].row()
            discipline_name = self.disciplines_tableView.model().index(selected_row, 2).data()

            confirm_dialog = ConfirmDeleteDialog(discipline_name)
            if confirm_dialog.exec_() == QtWidgets.QDialog.Accepted:
                num_group = self.disciplines_tableView.model().index(selected_row, 1).data()

                database.delete_disciplines(num_group, discipline_name)
                self.load_data_to_table()
        else:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Выберите дисциплину для удаления.")

    def load_data_to_table(self):
        num_group = self.disciplines_comboBox.currentText()
        disciplines_data = database.get_disciplines_by_num_group(num_group)
                
        model = QtGui.QStandardItemModel(len(disciplines_data), 3)

        model.setHorizontalHeaderLabels(['ID', 'NUM_GROUP', 'NAME'])

        for row, discipline in enumerate(disciplines_data):
            for column, data in enumerate(discipline):
                item = QtGui.QStandardItem(str(data))
                model.setItem(row, column, item)

        self.disciplines_tableView.setModel(model)

    def import_disciplines(self):
        import_manager.import_data('disciplines')
        self.load_data_to_combobox()
        self.load_data_to_table()

    
    def export_disciplines(self):
        export_manager.export_data('disciplines')
        self.load_data_to_combobox()
        self.load_data_to_table()
