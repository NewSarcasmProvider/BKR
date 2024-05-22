# File main.py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtWidgets
from forms.library import Ui_library
from forms.disciplines import Ui_disciplines
from forms.groups import Ui_groups
from forms.students import Ui_students
from forms.books import Ui_books
from forms.statistics import Ui_statistics

class Ui_Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Main")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # Кнопка для учета книг
        self.main_button_issuance_and_return_of_books = QtWidgets.QPushButton(self.centralwidget)
        self.main_button_issuance_and_return_of_books.setGeometry(QtCore.QRect(100, 200, 600, 40))
        self.main_button_issuance_and_return_of_books.setObjectName("main_button_issuance_and_return_of_books")
        
        # Кнопка "Добавление группы"
        self.main_button_adding_a_group = QtWidgets.QPushButton(self.centralwidget)
        self.main_button_adding_a_group.setGeometry(QtCore.QRect(100, 280, 280, 40))
        self.main_button_adding_a_group.setObjectName("main_button_adding_a_group")
        
        # Кнопка "Добавление дисциплины"
        self.main_button_adding_a_discipline = QtWidgets.QPushButton(self.centralwidget)
        self.main_button_adding_a_discipline.setGeometry(QtCore.QRect(420, 280, 280, 40))
        self.main_button_adding_a_discipline.setObjectName("main_button_adding_a_discipline")
        
        # Кнопка "Добавление учеников"
        self.main_button_adding_a_student = QtWidgets.QPushButton(self.centralwidget)
        self.main_button_adding_a_student.setGeometry(QtCore.QRect(100, 360, 280, 40))
        self.main_button_adding_a_student.setObjectName("main_button_adding_a_student")
        
        # Кнопка "Добавление книг"
        self.main_button_adding_a_book = QtWidgets.QPushButton(self.centralwidget)
        self.main_button_adding_a_book.setGeometry(QtCore.QRect(420, 360, 280, 40))
        self.main_button_adding_a_book.setObjectName("main_button_adding_a_book")

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        # Подключение сигналов к слотам
        self.main_button_issuance_and_return_of_books.clicked.connect(self.open_library_window)
        self.main_button_adding_a_group.clicked.connect(self.open_groups_window)
        self.main_button_adding_a_discipline.clicked.connect(self.open_discipline_window)
        self.main_button_adding_a_student.clicked.connect(self.open_student_window)
        self.main_button_adding_a_book.clicked.connect(self.open_books_window)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Main", "Меню"))
        self.main_button_issuance_and_return_of_books.setText(_translate("Main", "Учет книг"))
        self.main_button_adding_a_group.setText(_translate("Main", "Добавление группы"))
        self.main_button_adding_a_discipline.setText(_translate("Main", "Добавление дисциплины"))
        self.main_button_adding_a_student.setText(_translate("Main", "Добавление учеников"))
        self.main_button_adding_a_book.setText(_translate("Main", "Добавление книг"))

    def open_library_window(self):
        self.library_window = Ui_library(self)
        self.library_window.show()
        self.close()

    def open_groups_window(self):
        self.groups_window = Ui_groups(self)
        self.groups_window.show()
        self.close()

    def open_discipline_window(self):
        self.discipline_window = Ui_disciplines(self)
        self.discipline_window.show()
        self.close()

    def open_student_window(self):
        self.student_window = Ui_students(self)
        self.student_window.show()
        self.close()

    def open_books_window(self):
        self.books_window = Ui_books(self)
        self.books_window.show()
        self.close()

    def open_statistics_window(self):
        self.statistics_window = Ui_statistics(self)
        self.statistics_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Ui_Main()
    main_window.show()
    sys.exit(app.exec_())