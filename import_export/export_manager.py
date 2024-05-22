from PyQt5.QtWidgets import QFileDialog
import pandas as pd
from data.data import DatabaseManager 

database = DatabaseManager()

class ExportManager:
    def __init__(self):
        self.database = DatabaseManager()

    def export_data(self, data_type, num_group=None):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(None, "Выберите место для экспорта", "", "Excel Files (*.xlsx);;All Files (*)", options=options)
        if file_path:
            try:
                if data_type == 'students':
                    self.export_students_to_xlsx(file_path)
                elif data_type == 'disciplines':
                    self.export_disciplines_to_xlsx(file_path)
                elif data_type == 'books':
                    self.export_books_to_xlsx(file_path)
                elif data_type == 'library':
                    self.export_library_to_xlsx(file_path, num_group)
            except Exception as e:
                print(f"Произошла ошибка при экспорте {data_type}:", e)

    def export_books_to_xlsx(self, file_path):
        try:
            books = self.database.get_books()
            columns = ["ID","NUM_GROUP", "DISCIPLINES", "BOOK_NAME", "AUTHOR", "PUBLISHER", "YEAR_PUB", "YEAR_LICENSE_EXP"]
            df = pd.DataFrame(books, columns=columns)
            df.drop(columns=["ID"], inplace=True)
            df.to_excel(file_path, index=False)
            print("Книги успешно экспортированы в XLSX файл.")
        except Exception as e:
            print("Произошла ошибка при экспорте книг:", e)

    def export_disciplines_to_xlsx(self, file_path):
        try:
            disciplines = self.database.get_disciplines()
            columns = ["ID","NUM_GROUP", "DISCIPLINE_NAME"]
            df = pd.DataFrame(disciplines, columns=columns)
            df.drop(columns=["ID"], inplace=True)
            df.to_excel(file_path, index=False)
            print("Дисциплины успешно экспортированы в XLSX файл.")
        except Exception as e:
            print("Произошла ошибка при экспорте дисциплин:", e)

    def export_students_to_xlsx(self, file_path):
        try:
            students = self.database.get_students()
            columns = ["ID","NUM_GROUP", "STUDENT_NAME"]
            df = pd.DataFrame(students, columns=columns)
            df.drop(columns=["ID"], inplace=True)
            df.to_excel(file_path, index=False)
            print("Студенты успешно экспортированы в XLSX файл.")
        except Exception as e:
            print("Произошла ошибка при экспорте студентов:", e)

    def export_library_to_xlsx(self, file_path, num_group):
        try:
            disciplines_data = self.database.get_disciplines_by_num_group(num_group)
            name_disciplines_data = [row[2] for row in disciplines_data]

            students_data = self.database.get_students_by_num_group(num_group)
            name_students_data = [row[2] for row in students_data]

            data = { 'Student Name': name_students_data }
            for discipline in name_disciplines_data:
                values = [self.database.get_library_value(num_group, student, discipline) for student in name_students_data]
                data[discipline] = values

            df = pd.DataFrame(data)
            df.to_excel(file_path, index=False)
            print("Данные библиотеки успешно экспортированы в XLSX файл.")
        except Exception as e:
            print("Произошла ошибка при экспорте данных библиотеки:", e)
