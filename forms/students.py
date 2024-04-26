from PyQt5 import QtCore, QtGui, QtWidgets
from data.data import DatabaseManager

database = DatabaseManager()

class Ui_students(object):
    def setupUi(self, students):
        students.setObjectName("students")
        students.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(students)
        self.centralwidget.setObjectName("centralwidget")
        self.students_button_add = QtWidgets.QPushButton(self.centralwidget)
        self.students_button_add.setGeometry(QtCore.QRect(400, 20, 180, 30))
        self.students_button_add.setObjectName("students_button_add")
        self.students_button_delete = QtWidgets.QPushButton(self.centralwidget)
        self.students_button_delete.setGeometry(QtCore.QRect(600, 20, 180, 30))
        self.students_button_delete.setObjectName("students_button_delete")
        self.students_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.students_lineEdit.setGeometry(QtCore.QRect(20, 70, 761, 30))
        self.students_lineEdit.setObjectName("students_lineEdit")
        self.students_tableView = QtWidgets.QTableView(self.centralwidget)
        self.students_tableView.setGeometry(QtCore.QRect(20, 130, 760, 471))
        self.students_tableView.setObjectName("students_tableView")
        self.students_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.students_comboBox.setGeometry(QtCore.QRect(20, 20, 360, 30))
        self.students_comboBox.setObjectName("students_comboBox")
        students.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(students)
        self.statusbar.setObjectName("statusbar")
        students.setStatusBar(self.statusbar)

        self.retranslateUi(students)
        QtCore.QMetaObject.connectSlotsByName(students)

        # Заполняем combobox данными из базы данных
        self.load_data_to_combobox()

        # Подключаем сигнал к слоту
        self.students_comboBox.currentIndexChanged.connect(self.load_data_to_table)

        # Подключаем обработчик событий к кнопке students_button_add
        self.students_button_add.clicked.connect(self.add_students)

        # Подключаем обработчик событий к кнопке students_button_delete
        self.students_button_delete.clicked.connect(self.delete_students)

    def retranslateUi(self, students):
        _translate = QtCore.QCoreApplication.translate
        students.setWindowTitle(_translate("students", "MainWindow"))
        self.students_button_add.setText(_translate("students", "Добавить ученика"))
        self.students_button_delete.setText(_translate("students", "Удалить ученика"))

    def load_data_to_combobox(self):
        # Очищаем combobox перед загрузкой данных, чтобы избежать дублирования
        self.students_comboBox.clear()
        # Получаем данные из базы данных (предположим, что функция get_disciplines() возвращает список предметов)
        groups = database.get_groups()
        # Добавляем данные в combobox
        for groups in groups:
            self.students_comboBox.addItem(str(groups[1]))

    def add_students(self):
        # Получаем num_group из QLineEdit
        num_group = self.students_comboBox.currentText()
        students = self.students_lineEdit.text()
        database.create_students(num_group, students)
        self.load_data_to_table() 

    def delete_students(self):
        # Получаем num_group из QLineEdit
        num_group = self.students_comboBox.currentText()
        students = self.students_lineEdit.text()
        database.delete_students(num_group, students)
        self.load_data_to_table()

    def load_data_to_table(self):
        num_group = self.students_comboBox.currentText()
        # Получаем данные из базы данных
        students_data = database.get_students_by_num_group(num_group)
        
                
        # Создаем модель данных для отображения в таблице
        model = QtGui.QStandardItemModel(len(students_data), 3)  # 3 колонки: ID и NUM_GROUP, и NAME
                
        # Устанавливаем заголовки колонок
        model.setHorizontalHeaderLabels(['ID', 'NUM_GROUP', 'NAME'])
                
        # Заполняем модель данными из базы данных
        for row, students in enumerate(students_data):
            for column, data in enumerate(students):
                item = QtGui.QStandardItem(str(data))
                model.setItem(row, column, item)

        # Устанавливаем созданную модель данных в таблицу
        self.students_tableView.setModel(model)