from PyQt5 import QtCore, QtGui, QtWidgets
from forms.library import Ui_library
from forms.disciplines import Ui_disciplines
from forms.groups import Ui_groups
from forms.students import Ui_students
from forms.books import Ui_books

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.main_button_issuance_and_return_of_books = QtWidgets.QPushButton(self.centralwidget)
        self.main_button_issuance_and_return_of_books.setGeometry(QtCore.QRect(100, 200, 600, 40))
        self.main_button_issuance_and_return_of_books.setObjectName("main_button_issuance_and_return_of_books")
        self.main_button_adding_a_group = QtWidgets.QPushButton(self.centralwidget)
        self.main_button_adding_a_group.setGeometry(QtCore.QRect(100, 280, 280, 40))
        self.main_button_adding_a_group.setObjectName("main_button_adding_a_group")
        self.main_button_adding_a_discipline = QtWidgets.QPushButton(self.centralwidget)
        self.main_button_adding_a_discipline.setGeometry(QtCore.QRect(420, 280, 280, 40))
        self.main_button_adding_a_discipline.setObjectName("main_button_adding_a_discipline")
        self.main_button_adding_a_student = QtWidgets.QPushButton(self.centralwidget)
        self.main_button_adding_a_student.setGeometry(QtCore.QRect(100, 360, 280, 40))
        self.main_button_adding_a_student.setObjectName("main_button_adding_a_student")
        self.main_button_adding_a_book = QtWidgets.QPushButton(self.centralwidget)
        self.main_button_adding_a_book.setGeometry(QtCore.QRect(420, 360, 280, 40))
        self.main_button_adding_a_book.setObjectName("main_button_adding_a_book")
        Main.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

        # Соединяем событие нажатия кнопки с обработчиком
        self.main_button_issuance_and_return_of_books.clicked.connect(self.open_library_window)
        self.main_button_adding_a_group.clicked.connect(self.open_group_window)
        self.main_button_adding_a_discipline.clicked.connect(self.open_discipline_window)
        self.main_button_adding_a_student.clicked.connect(self.open_student_window)
        self.main_button_adding_a_book.clicked.connect(self.open_books_window)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "MainWindow"))
        self.main_button_issuance_and_return_of_books.setText(_translate("Main", "Учет книг"))
        self.main_button_adding_a_group.setText(_translate("Main", "Добавление группы"))
        self.main_button_adding_a_discipline.setText(_translate("Main", "Добавление дисциплины"))
        self.main_button_adding_a_student.setText(_translate("Main", "Добавление учеников"))
        self.main_button_adding_a_book.setText(_translate("Main", "Добавление книг"))

    def open_library_window(self):
        self.library_window = QtWidgets.QMainWindow()
        self.library_ui = Ui_library()
        self.library_ui.setupUi(self.library_window)
        self.library_window.show()

    def open_group_window(self):
        self.groups_window = QtWidgets.QMainWindow()
        self.groups_ui = Ui_groups()
        self.groups_ui.setupUi(self.groups_window)
        self.groups_window.show()

    def open_discipline_window(self):
        self.disciplines_window = QtWidgets.QMainWindow()
        self.disciplines_ui = Ui_disciplines()
        self.disciplines_ui.setupUi(self.disciplines_window)
        self.disciplines_window.show()

    def open_student_window(self):
        self.student_window = QtWidgets.QMainWindow()
        self.student_ui = Ui_students()
        self.student_ui.setupUi(self.student_window)
        self.student_window.show()

    def open_books_window(self):
        self.books_window = QtWidgets.QMainWindow()
        self.books_ui = Ui_books()
        self.books_ui.setupUi(self.books_window)
        self.books_window.show()
