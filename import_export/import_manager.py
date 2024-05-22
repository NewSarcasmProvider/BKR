import pandas as pd
from PyQt5.QtWidgets import QFileDialog
from data.data import DatabaseManager 

database = DatabaseManager()

class ImportManager:
    def __init__(self):
        self.database = DatabaseManager()

    def import_data(self, data_type):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(None, "Выберите файл для импорта", "", "Excel Files (*.xlsx);;All Files (*)", options=options)
        if file_path:
            if data_type == 'students':
                self.import_students_from_xlsx(file_path)
            elif data_type == 'disciplines':
                self.import_disciplines_from_xlsx(file_path)
            elif data_type == 'books':
                self.import_books_from_xlsx(file_path)

    def import_students_from_xlsx(self, file_path):
        try:
            df = pd.read_excel(file_path)
            for index, row in df.iterrows():
                num_group, student_name = row
                self.database.create_students(num_group, student_name)

            print("Студенты успешно импортированы из XLSX файла.")
        except Exception as e:
            print("Произошла ошибка при импорте студентов:", e)

    def import_disciplines_from_xlsx(self, file_path):
        try:
            df = pd.read_excel(file_path)
            for index, row in df.iterrows():
                num_group, discipline_name = row
                self.database.create_disciplines(num_group, discipline_name)

            print("Дисциплины успешно импортированы из XLSX файла.")
        except Exception as e:
            print("Произошла ошибка при импорте дисциплин:", e)

    def import_books_from_xlsx(self, file_path):
        try:
            df = pd.read_excel(file_path)
            for index, row in df.iterrows():
                num_group, discipline, book_name, author, publisher, year_pub, year_license_exp = row
                self.database.create_books(num_group, discipline, book_name, author, publisher, year_pub, year_license_exp)

            print("Книги успешно импортированы из XLSX файла.")
        except Exception as e:
            print("Произошла ошибка при импорте книг:", e)

