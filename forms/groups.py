# File groups.py

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlTableModel
from data.data import DatabaseManager
from forms.confirmdeletedialog import ConfirmDeleteDialog

database = DatabaseManager()

class Ui_groups(QtWidgets.QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setupUi(self)

    def setupUi(self, groups):
        groups.setObjectName("groups")
        groups.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(groups)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groups_back = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groups_back.sizePolicy().hasHeightForWidth())
        self.groups_back.setSizePolicy(sizePolicy)
        self.groups_back.setMinimumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.groups_back.setFont(font)
        self.groups_back.setObjectName("groups_back")
        self.verticalLayout.addWidget(self.groups_back)
        self.lower_group = QtWidgets.QHBoxLayout()
        self.lower_group.setObjectName("lower_group")
        self.groups_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groups_lineEdit.sizePolicy().hasHeightForWidth())
        self.groups_lineEdit.setSizePolicy(sizePolicy)
        self.groups_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.groups_lineEdit.setFont(font)
        self.groups_lineEdit.setObjectName("groups_lineEdit")
        self.lower_group.addWidget(self.groups_lineEdit)
        self.groups_button_delete = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groups_button_delete.sizePolicy().hasHeightForWidth())
        self.groups_button_delete.setSizePolicy(sizePolicy)
        self.groups_button_delete.setMinimumSize(QtCore.QSize(190, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.groups_button_delete.setFont(font)
        self.groups_button_delete.setObjectName("groups_button_delete")
        self.lower_group.addWidget(self.groups_button_delete)
        self.groups_button_add = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groups_button_add.sizePolicy().hasHeightForWidth())
        self.groups_button_add.setSizePolicy(sizePolicy)
        self.groups_button_add.setMinimumSize(QtCore.QSize(190, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.groups_button_add.setFont(font)
        self.groups_button_add.setObjectName("groups_button_add")
        self.lower_group.addWidget(self.groups_button_add)
        self.verticalLayout.addLayout(self.lower_group)
        self.groups_tableView = QtWidgets.QTableView(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.groups_tableView.setFont(font)
        self.groups_tableView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.groups_tableView.setObjectName("groups_tableView")
        self.verticalLayout.addWidget(self.groups_tableView)
        groups.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(groups)
        self.statusbar.setObjectName("statusbar")
        groups.setStatusBar(self.statusbar)

        self.retranslateUi(groups)
        QtCore.QMetaObject.connectSlotsByName(groups)

        self.model = QSqlTableModel()

        self.groups_tableView.setModel(self.model)

        self.groups_button_add.clicked.connect(self.add_group)
        self.groups_button_delete.clicked.connect(self.delete_group)
        self.groups_back.clicked.connect(self.go_back_to_main)

    def showEvent(self, event):
        super().showEvent(event)
        self.load_data_to_table()
    
    def retranslateUi(self, groups):
        _translate = QtCore.QCoreApplication.translate
        groups.setWindowTitle(_translate("groups", "Группы"))
        self.groups_back.setText(_translate("groups", "Назад"))
        self.groups_button_delete.setText(_translate("groups", "Удалить группу"))
        self.groups_button_add.setText(_translate("groups", "Добавить группу"))

    def go_back_to_main(self):
        self.close()
        self.main_window.show()

    def add_group(self):
        num_group = self.groups_lineEdit.text()
        database.create_group(num_group)
        self.load_data_to_table() 

    def delete_group(self):
        selected_index = self.groups_tableView.selectedIndexes()
        if selected_index:
            selected_row = selected_index[0].row()
            group_name = self.groups_tableView.model().index(selected_row, 1).data()

            confirm_dialog = ConfirmDeleteDialog(group_name)
            if confirm_dialog.exec_() == QtWidgets.QDialog.Accepted:

                database.delete_group(group_name)
                self.load_data_to_table()
        else:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Выберите дисциплину для удаления.")

    from PyQt5 import QtGui

    def load_data_to_table(self):
        groups = database.get_groups()
        sorted_groups = sorted(groups, key=lambda x: x[1])
        
        model = QtGui.QStandardItemModel(len(sorted_groups), 2)
        
        model.setHorizontalHeaderLabels(['ID', 'NUM_GROUP'])
        
        for row, group in enumerate(sorted_groups):
            for column, data in enumerate(group):
                item = QtGui.QStandardItem(str(data))
                model.setItem(row, column, item)
        
        self.groups_tableView.setModel(model)
        
        self.groups_tableView.horizontalHeader().setStretchLastSection(True)
