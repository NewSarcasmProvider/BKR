from PyQt5 import QtCore, QtGui, QtWidgets
from data.data import DatabaseManager

database = DatabaseManager()

class Ui_library(object):
    def setupUi(self, library):
        library.setObjectName("library")
        library.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(library)
        self.centralwidget.setObjectName("centralwidget")
        self.library_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.library_comboBox.setGeometry(QtCore.QRect(20, 20, 360, 30))
        self.library_comboBox.setObjectName("library_comboBox")
        self.library_button_statistics = QtWidgets.QPushButton(self.centralwidget)
        self.library_button_statistics.setGeometry(QtCore.QRect(420, 20, 360, 30))
        self.library_button_statistics.setObjectName("library_button_statistics")
        self.library_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.library_tableWidget.setGeometry(QtCore.QRect(20, 70, 760, 510))
        self.library_tableWidget.setObjectName("library_tableWidget")
        self.library_tableWidget.setColumnCount(0)
        self.library_tableWidget.setRowCount(0)
        library.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(library)
        self.statusbar.setObjectName("statusbar")
        library.setStatusBar(self.statusbar)

        self.retranslateUi(library)
        QtCore.QMetaObject.connectSlotsByName(library)

        # Заполняем combobox данными из базы данных
        self.load_data_to_combobox()

        # Подключаем сигнал к слоту
        self.library_comboBox.currentIndexChanged.connect(self.load_data_to_table)

    def retranslateUi(self, library):
        _translate = QtCore.QCoreApplication.translate
        library.setWindowTitle(_translate("library", "MainWindow"))
        self.library_button_statistics.setText(_translate("library", "Статистика"))

    
    def load_data_to_combobox(self):
        # Очищаем combobox перед загрузкой данных, чтобы избежать дублирования
        self.library_comboBox.clear()
        # Получаем данные из базы данных (предположим, что функция get_disciplines() возвращает список предметов)
        groups = database.get_groups()
        # Добавляем данные в combobox
        for groups in groups:
            self.library_comboBox.addItem(str(groups[1]))

    def load_data_to_table(self):
        # Очистка таблицы перед загрузкой новых данных
        self.library_tableWidget.clear()
        
        # Получение списка дисциплин для выбранной группы
        num_group = self.library_comboBox.currentText()
        disciplines_data = database.get_disciplines_by_num_group(num_group)
        name_disciplines_data = [row[2] for row in disciplines_data]
        
        # Заголовок таблицы - дисциплины
        self.library_tableWidget.setColumnCount(len(name_disciplines_data))
        self.library_tableWidget.setHorizontalHeaderLabels(name_disciplines_data)
        
        # Получение списка студентов для выбранной группы
        students_data = database.get_students_by_num_group(num_group)
        name_students_data = [row[2] for row in students_data]
        
        # Заголовки строк таблицы - студенты
        self.library_tableWidget.setRowCount(len(name_students_data))
        self.library_tableWidget.setVerticalHeaderLabels(name_students_data)

        for row in range(len(name_students_data)):
            for col in range(len(name_disciplines_data)):
                combo_box = QtWidgets.QComboBox()
                books_data = database.get_books_by_num_group_and_disciplines(num_group, name_disciplines_data[col])
                combo_box.addItem("не выдана")
                for book_data in books_data:
                    combo_box.addItem(str(book_data[3]))
                    
                # Устанавливаем ранее выбранное значение, если оно существует
                current_value = database.get_library_value(num_group, name_students_data[row], name_disciplines_data[col])
                index = combo_box.findText(current_value)
                if index != -1:
                    combo_box.setCurrentIndex(index)
                self.library_tableWidget.setCellWidget(row, col, combo_box)


                combo_box.currentIndexChanged.connect(lambda index, num_group=num_group, student=name_students_data[row], discipline=name_disciplines_data[col], combo_box=combo_box: self.update_database_value(num_group, student, discipline, combo_box.currentText()))

    def update_database_value(self, num_group, student, discipline, value):
        database.update_database_value(num_group, student, discipline, value)

