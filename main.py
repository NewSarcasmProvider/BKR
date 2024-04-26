import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from forms.start import Ui_Main  # Импортируем класс Ui_Main из start.py

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Main()  # Создаем экземпляр класса Ui_Main
        self.ui.setupUi(self)  # Настраиваем интерфейс
        self.show()  # Показываем главное окно

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Main()
    sys.exit(app.exec_())
