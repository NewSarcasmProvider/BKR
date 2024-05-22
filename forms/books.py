# File books.py

from PyQt5 import QtCore, QtGui, QtWidgets
import openpyxl
from PyQt5.QtWidgets import QFileDialog
from data.data import DatabaseManager
from forms.confirmdeletedialog import ConfirmDeleteDialog
from import_export.import_manager import ImportManager
from import_export.export_manager import ExportManager

database = DatabaseManager()
import_manager = ImportManager()
export_manager = ExportManager()

class AddBookDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Добавить книгу")
        self.resize(400, 300)
        
        layout = QtWidgets.QVBoxLayout()

        self.num_group_label = QtWidgets.QLabel("NUM_GROUP:")
        self.num_group_combo = QtWidgets.QComboBox()
        layout.addWidget(self.num_group_label)
        layout.addWidget(self.num_group_combo)

        self.disciplines_label = QtWidgets.QLabel("DISCIPLINES:")
        self.disciplines_combo = QtWidgets.QComboBox()
        layout.addWidget(self.disciplines_label)
        layout.addWidget(self.disciplines_combo)

        self.name_label = QtWidgets.QLabel("NAME:")
        self.name_input = QtWidgets.QLineEdit()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        self.author_label = QtWidgets.QLabel("AUTHOR:")
        self.author_input = QtWidgets.QLineEdit()
        layout.addWidget(self.author_label)
        layout.addWidget(self.author_input)

        self.publisher_label = QtWidgets.QLabel("PUBLISHER:")
        self.publisher_input = QtWidgets.QLineEdit()
        layout.addWidget(self.publisher_label)
        layout.addWidget(self.publisher_input)

        self.year_pub_label = QtWidgets.QLabel("YEAR_PUB:")
        self.year_pub_input = QtWidgets.QLineEdit()
        layout.addWidget(self.year_pub_label)
        layout.addWidget(self.year_pub_input)

        self.year_license_exp_label = QtWidgets.QLabel("YEAR_LICENSE_EXP:")
        self.year_license_exp_input = QtWidgets.QLineEdit()
        layout.addWidget(self.year_license_exp_label)
        layout.addWidget(self.year_license_exp_input)

        self.add_button = QtWidgets.QPushButton("Добавить")
        layout.addWidget(self.add_button)

        self.setLayout(layout)

        self.add_button.clicked.connect(self.accept)
        
        self.load_data_to_combobox()

    def load_data_to_combobox(self):
        self.num_group_combo.clear()
        groups = database.get_groups()
        for group in groups:
            self.num_group_combo.addItem(str(group[1]))

        self.disciplines_combo.clear()
        disciplines = database.get_disciplines()
        for discipline in disciplines:
            self.disciplines_combo.addItem(str(discipline[2]))

    def get_data(self):
        return {
            'num_group': self.num_group_combo.currentText(),
            'disciplines': self.disciplines_combo.currentText(),
            'name': self.name_input.text(),
            'author': self.author_input.text(),
            'publisher': self.publisher_input.text(),
            'year_pub': self.year_pub_input.text(),
            'year_license_exp': self.year_license_exp_input.text(),
        }

class Ui_books(QtWidgets.QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setupUi(self)

    def setupUi(self, books):
        books.setObjectName("books")
        books.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(books)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.books_back = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.books_back.sizePolicy().hasHeightForWidth())
        self.books_back.setSizePolicy(sizePolicy)
        self.books_back.setMinimumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.books_back.setFont(font)
        self.books_back.setObjectName("books_back")
        self.verticalLayout.addWidget(self.books_back)
        self.upper_group = QtWidgets.QHBoxLayout()
        self.upper_group.setObjectName("upper_group")
        self.groups_button_import = QtWidgets.QPushButton(self.centralwidget)
        self.groups_button_import.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.groups_button_import.setFont(font)
        self.groups_button_import.setObjectName("groups_button_import")
        self.upper_group.addWidget(self.groups_button_import)
        self.groups_button_export = QtWidgets.QPushButton(self.centralwidget)
        self.groups_button_export.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.groups_button_export.setFont(font)
        self.groups_button_export.setObjectName("groups_button_export")
        self.upper_group.addWidget(self.groups_button_export)
        self.verticalLayout.addLayout(self.upper_group)
        self.lower_group = QtWidgets.QHBoxLayout()
        self.lower_group.setObjectName("lower_group")
        self.books_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.books_comboBox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.books_comboBox.setFont(font)
        self.books_comboBox.setObjectName("books_comboBox")
        self.lower_group.addWidget(self.books_comboBox)
        self.books_comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.books_comboBox_2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.books_comboBox_2.setFont(font)
        self.books_comboBox_2.setObjectName("books_comboBox_2")
        self.lower_group.addWidget(self.books_comboBox_2)
        self.books_button_add = QtWidgets.QPushButton(self.centralwidget)
        self.books_button_add.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.books_button_add.setFont(font)
        self.books_button_add.setObjectName("books_button_add")
        self.lower_group.addWidget(self.books_button_add)
        self.books_button_delete = QtWidgets.QPushButton(self.centralwidget)
        self.books_button_delete.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.books_button_delete.setFont(font)
        self.books_button_delete.setObjectName("books_button_delete")
        self.lower_group.addWidget(self.books_button_delete)
        self.verticalLayout.addLayout(self.lower_group)
        self.books_tableView = QtWidgets.QTableView(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.books_tableView.setFont(font)
        self.books_tableView.setObjectName("books_tableView")
        self.verticalLayout.addWidget(self.books_tableView)
        books.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(books)
        self.statusbar.setObjectName("statusbar")
        books.setStatusBar(self.statusbar)

        self.retranslateUi(books)
        QtCore.QMetaObject.connectSlotsByName(books)

        self.books_comboBox.currentIndexChanged.connect(self.load_data_to_table)
        self.books_comboBox_2.currentIndexChanged.connect(self.load_data_to_table)

        self.books_button_add.clicked.connect(self.add_books)
        self.books_button_delete.clicked.connect(self.delete_books)
        self.books_back.clicked.connect(self.go_back_to_main)

        self.groups_button_import.clicked.connect(self.import_books)
        self.groups_button_export.clicked.connect(self.export_books)

    def showEvent(self, event):
        super().showEvent(event)
        self.load_data_to_combobox()
        self.load_data_to_table()

    def retranslateUi(self, books):
        _translate = QtCore.QCoreApplication.translate
        books.setWindowTitle(_translate("books", "MainWindow"))
        self.books_back.setText(_translate("books", "Назад"))
        self.groups_button_import.setText(_translate("books", "Имрпорт"))
        self.groups_button_export.setText(_translate("books", "Экспорт"))
        self.books_button_add.setText(_translate("books", "Добавить книгу"))
        self.books_button_delete.setText(_translate("books", "Удалить книгу"))

    def go_back_to_main(self):
        self.close() 
        self.main_window.show()
    
    def load_data_to_combobox(self):
        self.books_comboBox.clear()
        groups = database.get_groups()
        sorted_groups = sorted(groups, key=lambda x: x[1])
        for group in sorted_groups:
            self.books_comboBox.addItem(str(group[1]))

        self.books_comboBox_2.clear()
        disciplines = database.get_disciplines()
        for disciplines in disciplines:
            self.books_comboBox_2.addItem(str(disciplines[2]))
    
    def add_books(self):
        dialog = AddBookDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            data = dialog.get_data()
            num_group = data['num_group']
            disciplines = data['disciplines']
            name = data['name']
            author = data['author']
            publisher = data['publisher']
            year_pub = data['year_pub']
            year_license_exp = data['year_license_exp']
            database.create_books(num_group, disciplines, name, author, publisher, year_pub, year_license_exp)
            self.load_data_to_table()
    
    def delete_books(self):
        selected_index = self.books_tableView.selectedIndexes()
        if selected_index:
            selected_row = selected_index[0].row()
            book_name = self.books_tableView.model().index(selected_row, 3).data()

            confirm_dialog = ConfirmDeleteDialog(book_name)
            if confirm_dialog.exec_() == QtWidgets.QDialog.Accepted:
                num_group = self.books_tableView.model().index(selected_row, 1).data()
                disciplines = self.books_tableView.model().index(selected_row, 2).data()

                database.delete_books(num_group, disciplines, book_name)
                self.load_data_to_table()
        else:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Выберите книгу для удаления.")

    def load_data_to_table(self):
        num_group = self.books_comboBox.currentText()
        discipline = self.books_comboBox_2.currentText()
        books_data = database.get_books_by_num_group_and_disciplines(num_group, discipline)

        model = QtGui.QStandardItemModel(len(books_data), 7)
        model.setHorizontalHeaderLabels(['ID', 'NUM_GROUP', 'DISCIPLINES', 'NAME', 'AUTHOR', 'PUBLISHER', 'YEAR_PUB', 'YEAR_LICENSE_EXP'])

        for row, books in enumerate(books_data):
            for column, data in enumerate(books):
                item = QtGui.QStandardItem(str(data))
                model.setItem(row, column, item)

        self.books_tableView.setModel(model)

    def import_books(self):
        import_manager.import_data('books')
        self.load_data_to_table()

    
    def export_books(self):
        export_manager.export_data('books')
        self.load_data_to_table()