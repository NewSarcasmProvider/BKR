from PyQt5 import QtCore, QtGui, QtWidgets
from data.data import DatabaseManager

database = DatabaseManager()

class Ui_disciplines(object):
    def setupUi(self, disciplines):
        disciplines.setObjectName("disciplines")
        disciplines.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(disciplines)
        self.centralwidget.setObjectName("centralwidget")
        self.disciplines_button_add = QtWidgets.QPushButton(self.centralwidget)
        self.disciplines_button_add.setGeometry(QtCore.QRect(400, 20, 180, 30))
        self.disciplines_button_add.setObjectName("disciplines_button_add")
        self.disciplines_button_delete = QtWidgets.QPushButton(self.centralwidget)
        self.disciplines_button_delete.setGeometry(QtCore.QRect(600, 20, 180, 30))
        self.disciplines_button_delete.setObjectName("disciplines_button_delete")
        self.disciplines_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.disciplines_lineEdit.setGeometry(QtCore.QRect(20, 70, 761, 30))
        self.disciplines_lineEdit.setObjectName("disciplines_lineEdit")
        self.disciplines_tableView = QtWidgets.QTableView(self.centralwidget)
        self.disciplines_tableView.setGeometry(QtCore.QRect(20, 130, 760, 471))
        self.disciplines_tableView.setObjectName("disciplines_tableView")
        self.disciplines_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.disciplines_comboBox.setGeometry(QtCore.QRect(20, 20, 360, 30))
        self.disciplines_comboBox.setObjectName("disciplines_comboBox")
        disciplines.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(disciplines)
        self.statusbar.setObjectName("statusbar")
        disciplines.setStatusBar(self.statusbar)

        self.retranslateUi(disciplines)
        QtCore.QMetaObject.connectSlotsByName(disciplines)

        # Заполняем combobox данными из базы данных
        self.load_data_to_combobox()

        # Подключаем сигнал к слоту
        self.disciplines_comboBox.currentIndexChanged.connect(self.load_data_to_table)

        # Подключаем обработчик событий к кнопке disciplines_button_add
        self.disciplines_button_add.clicked.connect(self.add_disciplines)

        # Подключаем обработчик событий к кнопке disciplines_button_delete
        self.disciplines_button_delete.clicked.connect(self.delete_disciplines)

    def retranslateUi(self, disciplines):
        _translate = QtCore.QCoreApplication.translate
        disciplines.setWindowTitle(_translate("disciplines", "MainWindow"))
        self.disciplines_button_add.setText(_translate("disciplines", "Добавить предмет"))
        self.disciplines_button_delete.setText(_translate("disciplines", "Удалить предмет"))

    def load_data_to_combobox(self):
        # Очищаем combobox перед загрузкой данных, чтобы избежать дублирования
        self.disciplines_comboBox.clear()
        # Получаем данные из базы данных (предположим, что функция get_disciplines() возвращает список предметов)
        groups = database.get_groups()
        # Добавляем данные в combobox
        for groups in groups:
            self.disciplines_comboBox.addItem(str(groups[1]))

    def add_disciplines(self):
        # Получаем num_group из QLineEdit
        num_group = self.disciplines_comboBox.currentText()
        disciplines = self.disciplines_lineEdit.text()
        database.create_disciplines(num_group, disciplines)
        self.load_data_to_table() 

    def delete_disciplines(self):
        # Получаем num_group из QLineEdit
        num_group = self.disciplines_comboBox.currentText()
        disciplines = self.disciplines_lineEdit.text()
        database.delete_disciplines(num_group, disciplines)
        self.load_data_to_table()

    def load_data_to_table(self):
        num_group = self.disciplines_comboBox.currentText()
        # Получаем данные из базы данных
        disciplines_data = database.get_disciplines_by_num_group(num_group)
                
        # Создаем модель данных для отображения в таблице
        model = QtGui.QStandardItemModel(len(disciplines_data), 3)  # 3 колонки: ID и NUM_GROUP, и NAME
                
        # Устанавливаем заголовки колонок
        model.setHorizontalHeaderLabels(['ID', 'NUM_GROUP', 'NAME'])
                
        # Заполняем модель данными из базы данных
        for row, discipline in enumerate(disciplines_data):
            for column, data in enumerate(discipline):
                item = QtGui.QStandardItem(str(data))
                model.setItem(row, column, item)

        # Устанавливаем созданную модель данных в таблицу
        self.disciplines_tableView.setModel(model)

