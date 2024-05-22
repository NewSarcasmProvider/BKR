from PyQt5 import QtWidgets

class ConfirmDeleteDialog(QtWidgets.QDialog):
    def __init__(self, name):
        super().__init__()
        self.setWindowTitle("Подтвердить удаление")
        self.resize(300, 100)

        layout = QtWidgets.QVBoxLayout()

        message_label = QtWidgets.QLabel(f"Вы уверены, что хотите удалить '{name}'?")
        layout.addWidget(message_label)

        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Yes | QtWidgets.QDialogButtonBox.No)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

        self.setLayout(layout)