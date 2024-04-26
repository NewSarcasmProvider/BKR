from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlTableModel
from data.data import DatabaseManager

database = DatabaseManager()

class Ui_groups(object):
    def setupUi(self, groups):
        groups.setObjectName("groups")
        groups.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(groups)
        self.centralwidget.setObjectName("centralwidget")
        self.groups_button_add = QtWidgets.QPushButton(self.centralwidget)
        self.groups_button_add.setGeometry(QtCore.QRect(400, 20, 180, 30))
        self.groups_button_add.setObjectName("groups_button_add")
        self.groups_button_delete = QtWidgets.QPushButton(self.centralwidget)
        self.groups_button_delete.setGeometry(QtCore.QRect(600, 20, 180, 30))
        self.groups_button_delete.setObjectName("groups_button_delete")
        self.groups_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.groups_lineEdit.setGeometry(QtCore.QRect(20, 20, 360, 30))
        self.groups_lineEdit.setObjectName("groups_lineEdit")
        self.groups_tableView = QtWidgets.QTableView(self.centralwidget)
        self.groups_tableView.setGeometry(QtCore.QRect(20, 70, 760, 510))
        self.groups_tableView.setObjectName("groups_tableView")
        groups.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(groups)
        self.statusbar.setObjectName("statusbar")
        groups.setStatusBar(self.statusbar)

        self.retranslateUi(groups)
        QtCore.QMetaObject.connectSlotsByName(groups)

        # Подключаем обработчик событий к кнопке groups_button_add
        self.groups_button_add.clicked.connect(self.add_group)

        # Подключаем обработчик событий к кнопке groups_button_delete
        self.groups_button_delete.clicked.connect(self.delete_group)

        # Создаем модель данных и связываем ее с таблицей
        self.model = QSqlTableModel()
        self.groups_tableView.setModel(self.model)

        # Заполняем таблицу данными из базы данных при открытии окна
        self.load_data_to_table()

    def retranslateUi(self, groups):
        _translate = QtCore.QCoreApplication.translate
        groups.setWindowTitle(_translate("groups", "MainWindow"))
        self.groups_button_add.setText(_translate("groups", "Добавить группу"))
        self.groups_button_delete.setText(_translate("groups", "Удалить группу"))

    def add_group(self):
        # Получаем num_group из QLineEdit
        num_group = self.groups_lineEdit.text()
        database.create_group(num_group)
        self.load_data_to_table() 

    def delete_group(self):
        # Получаем num_group из QLineEdit
        num_group = self.groups_lineEdit.text()
        database.delete_group(num_group)
        self.load_data_to_table() 

    def load_data_to_table(self):
         # Получаем данные из базы данных
        groups = database.get_groups()
        
        # Создаем модель данных для отображения в таблице
        model = QtGui.QStandardItemModel(len(groups), 2)  # 2 колонки: ID и NUM_GROUP
        
        # Устанавливаем заголовки колонок
        model.setHorizontalHeaderLabels(['ID', 'NUM_GROUP'])
        
        # Заполняем модель данными из базы данных
        for row, group in enumerate(groups):
            for column, data in enumerate(group):
                item = QtGui.QStandardItem(str(data))
                model.setItem(row, column, item)
        
        # Устанавливаем созданную модель данных в таблицу
        self.groups_tableView.setModel(model)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    groups = QtWidgets.QMainWindow()
    ui = Ui_groups()
    ui.setupUi(groups)
    groups.show()
    sys.exit(app.exec_())
