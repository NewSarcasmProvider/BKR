from PyQt5 import QtCore, QtGui, QtWidgets
from data.data import DatabaseManager

database = DatabaseManager()

class Ui_books(object):
    def setupUi(self, books):
        books.setObjectName("books")
        books.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(books)
        self.centralwidget.setObjectName("centralwidget")
        self.books_button_add = QtWidgets.QPushButton(self.centralwidget)
        self.books_button_add.setGeometry(QtCore.QRect(520, 20, 120, 30))
        self.books_button_add.setObjectName("books_button_add")
        self.books_button_delete = QtWidgets.QPushButton(self.centralwidget)
        self.books_button_delete.setGeometry(QtCore.QRect(660, 20, 120, 30))
        self.books_button_delete.setObjectName("books_button_delete")
        self.books_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.books_lineEdit.setGeometry(QtCore.QRect(20, 70, 761, 30))
        self.books_lineEdit.setObjectName("books_lineEdit")
        self.books_tableView = QtWidgets.QTableView(self.centralwidget)
        self.books_tableView.setGeometry(QtCore.QRect(20, 130, 760, 471))
        self.books_tableView.setObjectName("books_tableView")
        self.books_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.books_comboBox.setGeometry(QtCore.QRect(20, 20, 230, 30))
        self.books_comboBox.setObjectName("books_comboBox")
        self.books_comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.books_comboBox_2.setGeometry(QtCore.QRect(270, 20, 230, 30))
        self.books_comboBox_2.setObjectName("books_comboBox_2")
        books.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(books)
        self.statusbar.setObjectName("statusbar")
        books.setStatusBar(self.statusbar)

        self.retranslateUi(books)
        QtCore.QMetaObject.connectSlotsByName(books)

        # Заполняем combobox данными из базы данных
        self.load_data_to_combobox()

        # Подключаем сигнал к слоту
        self.books_comboBox.currentIndexChanged.connect(self.load_data_to_table)
        self.books_comboBox_2.currentIndexChanged.connect(self.load_data_to_table)

        # Подключаем обработчик событий к кнопке disciplines_button_add
        self.books_button_add.clicked.connect(self.add_books)

        # Подключаем обработчик событий к кнопке disciplines_button_delete
        self.books_button_delete.clicked.connect(self.delete_books)

    def retranslateUi(self, books):
        _translate = QtCore.QCoreApplication.translate
        books.setWindowTitle(_translate("books", "MainWindow"))
        self.books_button_add.setText(_translate("books", "Добавить книгу"))
        self.books_button_delete.setText(_translate("books", "Удалить книгу"))

    def load_data_to_combobox(self):
        # Очищаем combobox перед загрузкой данных, чтобы избежать дублирования
        self.books_comboBox.clear()
        # Получаем данные из базы данных (предположим, что функция get_disciplines() возвращает список предметов)
        groups = database.get_groups()
        # Добавляем данные в combobox
        for groups in groups:
            self.books_comboBox.addItem(str(groups[1]))

        # Очищаем combobox перед загрузкой данных, чтобы избежать дублирования
        self.books_comboBox_2.clear()
        # Получаем данные из базы данных (предположим, что функция get_disciplines() возвращает список предметов)
        disciplines = database.get_disciplines()
        # Добавляем данные в combobox
        for disciplines in disciplines:
            self.books_comboBox_2.addItem(str(disciplines[2]))

    def add_books(self):
        num_group = self.books_comboBox.currentText()
        disciplines = self.books_comboBox_2.currentText()

        books = self.books_lineEdit.text()
        database.create_books(num_group, disciplines, books)
        self.load_data_to_table() 

    def delete_books(self):
        num_group = self.books_comboBox.currentText()
        
        disciplines = self.books_comboBox_2.currentText()
        books = self.books_lineEdit.text()
        database.delete_books(num_group, disciplines, books)
        self.load_data_to_table()

    def load_data_to_table(self):
        num_group = self.books_comboBox.currentText()
        disciplines = self.books_comboBox_2.currentText()
        # Получаем данные из базы данных
        books_data = database.get_books_by_num_group_and_disciplines(num_group, disciplines)

        # Создаем модель данных для отображения в таблице
        model = QtGui.QStandardItemModel(len(books_data), 4)
                
        # Устанавливаем заголовки колонок
        model.setHorizontalHeaderLabels(['ID', 'NUM_GROUP', 'ID_DISCIP', 'NAME'])
                
        # Заполняем модель данными из базы данных
        for row, books in enumerate(books_data):
            for column, data in enumerate(books):
                item = QtGui.QStandardItem(str(data))
                model.setItem(row, column, item)

        # Устанавливаем созданную модель данных в таблицу
        self.books_tableView.setModel(model)
