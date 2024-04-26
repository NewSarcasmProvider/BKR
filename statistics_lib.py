from data.data import DatabaseManager

def calculate_book_issue_percentage(database_manager):
    try:
        groups = database_manager.get_groups()
        for group in groups:
            group_num = group[1]

            print(f"Статистика по группе {group_num}:")

            # Получаем список студентов в текущей группе
            students = database_manager.get_students_by_num_group(group_num)
            for student in students:
                student_name = student[2]

                # Получаем количество выданных книг для текущего студента
                issued_books_count = 0
                disciplines = database_manager.get_disciplines_by_num_group(group_num)
                for discipline in disciplines:
                    discipline_name = discipline[2]

                    # Получаем значение книги для текущего студента и дисциплины
                    book_value = database_manager.get_library_value(group_num, student_name, discipline_name)
                    if book_value is not None and book_value != "не выдана":
                        issued_books_count += 1

                # Получаем общее количество дисциплин для текущего студента
                total_disciplines_count = len(disciplines)

                # Вычисляем процент выданных книг для текущего студента
                if total_disciplines_count > 0:
                    percentage = (issued_books_count / total_disciplines_count) * 100
                else:
                    percentage = 0

                print(f"Студент {student_name}: {percentage:.2f}% книг выдано.")

    except Exception as e:
        print("Ошибка при вычислении статистики:", e)

# Пример использования

db_manager = DatabaseManager()
calculate_book_issue_percentage(db_manager)
