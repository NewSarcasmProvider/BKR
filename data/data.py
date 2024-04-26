import sqlite3

class DatabaseManager:
    def __init__(self):
        self.databaseConnect = sqlite3.connect("lib.db")
        self.cursor = self.databaseConnect.cursor()
        self.createTable()

    def __del__(self):
        self.databaseConnect.close()

    def createTable(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS \"books\" (\
            \"ID\"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
            \"NUM_GROUP\" INTEGER NOT NULL,\
            \"ID_DISCIP\" INTEGER NOT NULL,\
            \"NAME\"  TEXT NOT NULL)")
        self.databaseConnect.commit()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS \"groups\" (\
            \"ID\"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
            \"NUM_GROUP\" INTEGER NOT NULL UNIQUE)")
        self.databaseConnect.commit()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS \"disciplines\" (\
            \"ID\"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
            \"NUM_GROUP\" INTEGER NOT NULL,\
            \"NAME\"  TEXT NOT NULL)")
        self.databaseConnect.commit()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS \"students\" (\
            \"ID\"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
            \"NUM_GROUP\" INTEGER NOT NULL,\
            \"NAME\"  TEXT NOT NULL)")
        self.databaseConnect.commit()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS \"library\" (\
            \"ID\"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
            \"NUM_GROUP\" INTEGER NOT NULL,\
            \"ID_STUDENT\"    INTEGER NOT NULL,\
            \"ID_DISCIP\" INTEGER NOT NULL,\
            \"BOOK\" INTEGER)")
        self.databaseConnect.commit()

    # group
    def create_group(self, num_group):
        """
        Создает новую запись в таблице 'groups' с указанным номером группы.

        :param num_group: Номер группы для добавления.
        """
        try:
            self.cursor.execute("INSERT INTO groups (NUM_GROUP) VALUES (?)", (num_group,))
            self.databaseConnect.commit()
            print(f"Группа с номером {num_group} успешно добавлена в базу данных.")
        except sqlite3.Error as e:
            print("Ошибка при добавлении группы в базу данных:", e)

    def delete_group(self, num_group):
        """
        Удаляет группу с указанным номером из таблицы 'groups' и все связанные с ней записи из других таблиц.

        :param num_group: Номер группы для удаления.
        """
        try:
            # Удаляем все записи связанные с этой группой из других таблиц
            self.cursor.execute("DELETE FROM library WHERE NUM_GROUP = ?", (num_group,))
            self.cursor.execute("DELETE FROM disciplines WHERE NUM_GROUP = ?", (num_group,))
            self.cursor.execute("DELETE FROM students WHERE NUM_GROUP = ?", (num_group,))
            self.databaseConnect.commit()

            # Удаляем группу из таблицы 'groups'
            self.cursor.execute("DELETE FROM groups WHERE NUM_GROUP = ?", (num_group,))
            self.databaseConnect.commit()

            print(f"Группа с номером {num_group} успешно удалена из базы данных.")
        except sqlite3.Error as e:
            print("Ошибка при удалении группы из базы данных:", e)

    def get_groups(self):
        try:
            self.cursor.execute("SELECT * FROM groups")
            self.databaseConnect.commit()
        except sqlite3.Error as e:
            print("Ошибка при запросе группы из базы данных:", e)
        else:
            return self.cursor.fetchall()
        
    # disciplines
    def create_disciplines(self, num_group, disciplines):
        """
        Создать дисциплины для определенной группы.

        :param num_group: Номер группы.
        :param disciplines: Список названий дисциплин для добавления.
        """
        try:
            self.cursor.execute("INSERT INTO disciplines (NUM_GROUP, NAME) VALUES (?, ?)",(num_group, disciplines))
            self.databaseConnect.commit()
            print(f"Дисциплина {disciplines} группы {num_group} успешно добавлена в базы данных.")
        except sqlite3.Error as e:
            print("Ошибка при добавлении дисциплин:", e)

    def delete_disciplines(self, num_group, disciplines):
        """
        Удаляет указанные дисциплины из таблицы 'disciplines' и все связанные с ними записи из других таблиц.

        :param disciplines: Список названий дисциплин для удаления.
        """
        try:

            # Удаляем все записи связанные с этими дисциплинами из других таблиц
            self.cursor.execute("DELETE FROM library WHERE ID_DISCIP IN (SELECT ID FROM disciplines WHERE NAME = ? AND NUM_GROUP = ?)", (disciplines, num_group))
            self.databaseConnect.commit()

            # Удаляем дисциплины из таблицы 'disciplines'
            self.cursor.execute("DELETE FROM disciplines WHERE NAME = ? AND NUM_GROUP = ?", (disciplines, num_group))
            self.databaseConnect.commit()

            print(f"Дисциплина {disciplines} группы {num_group} успешно удалена из базы данных.")
        except sqlite3.Error as e:
            print("Ошибка при удалении дисциплин из базы данных:", e)

    def get_disciplines(self):
        try:
            self.cursor.execute("SELECT * FROM disciplines")
            self.databaseConnect.commit()
        except sqlite3.Error as e:
            print("Ошибка при запросе дисциплин из базы данных:", e)
        else:
            return self.cursor.fetchall()
        
    def get_disciplines_by_num_group(self, num_group):
        try:
            self.cursor.execute("SELECT * FROM disciplines WHERE NUM_GROUP=?", (num_group,))
            self.databaseConnect.commit()
        except sqlite3.Error as e:
            print("Ошибка при запросе дисциплин из базы данных:", e)
        else:
            return self.cursor.fetchall()

    # students
    def create_students(self, num_group, students):
        """
        Создать студента для определенной группы.

        :param num_group: Номер группы.
        :param students: Имя студента для добавления.
        """
        try:
            self.cursor.execute("INSERT INTO students (NUM_GROUP, NAME) VALUES (?, ?)",(num_group, students))
            self.databaseConnect.commit()
            print(f"Студент {students} группы {num_group} успешно добавлен в базы данных.")
        except sqlite3.Error as e:
            print("Ошибка при добавлении студента:", e)

    def delete_students(self, num_group, students):
        """
        Удаляет указанные дисциплины из таблицы 'students' и все связанные с ними записи из других таблиц.

        :param students: Имя студента для удаления.
        """
        try:

            # Удаляем все записи связанные с этими дисциплинами из других таблиц
            self.cursor.execute("DELETE FROM library WHERE ID_DISCIP IN (SELECT ID FROM students WHERE NAME = ? AND NUM_GROUP = ?)", (students, num_group))
            self.databaseConnect.commit()

            # Удаляем дисциплины из таблицы 'students'
            self.cursor.execute("DELETE FROM students WHERE NAME = ? AND NUM_GROUP = ?", (students, num_group))
            self.databaseConnect.commit()

            print(f"Студент {students} группы {num_group} успешно удалена из базы данных.")
        except sqlite3.Error as e:
            print("Ошибка при удалении дисциплин из базы данных:", e)

    def get_students(self):
        try:
            self.cursor.execute("SELECT * FROM students")
            self.databaseConnect.commit()
        except sqlite3.Error as e:
            print("Ошибка при запросе дисциплин из базы данных:", e)
        else:
            return self.cursor.fetchall()
        
    def get_students_by_num_group(self, num_group):
        try:
            self.cursor.execute("SELECT * FROM students WHERE NUM_GROUP=?", (num_group,))
            self.databaseConnect.commit()
        except sqlite3.Error as e:
            print("Ошибка при запросе дисциплин из базы данных:", e)
        else:
            return self.cursor.fetchall()

    # books
    def create_books(self, num_group, disciplines, books):
        """
        Создать книгу для определенной группы и дисциплины.

        :param num_group: Номер группы.
        :param disciplines: Дисциплина
        :param books: Название книги для добавления.
        """
        try:
            self.cursor.execute("INSERT INTO books (NUM_GROUP, ID_DISCIP, NAME) VALUES (?, ?, ?)",(num_group, disciplines, books))
            self.databaseConnect.commit()
            print(f"Студент {books} группы {num_group} и дисциплины {disciplines} успешно добавлен в базы данных.")
        except sqlite3.Error as e:
            print("Ошибка при добавлении студента:", e)

    def delete_books(self, num_group, disciplines, books):
        """
        Удалить книгу из базы данных.

        :param num_group: Номер группы.
        :param disciplines: Дисциплина.
        :param books: Название книги для удаления.
        """
        try:
            # Удаляем связанные записи из таблицы library
            self.cursor.execute("DELETE FROM library WHERE NUM_GROUP = ? AND ID_DISCIP = ? AND BOOK = ?", (num_group, disciplines, books))
            self.databaseConnect.commit()
            print(f"Связанные записи в таблице library для книги {books} успешно удалены.")
            
            # Удаляем книгу из таблицы books
            self.cursor.execute("DELETE FROM books WHERE NUM_GROUP = ? AND ID_DISCIP = ? AND NAME = ?", (num_group, disciplines, books))
            self.databaseConnect.commit()
            print(f"Книга {books} для группы {num_group} и дисциплины {disciplines} успешно удалена из базы данных.")
            
        except sqlite3.Error as e:
            print("Ошибка при удалении книги:", e)

    def get_students(self):
        try:
            self.cursor.execute("SELECT * FROM books")
            self.databaseConnect.commit()
        except sqlite3.Error as e:
            print("Ошибка при получении списка книг:", e)
        else:
            return self.cursor.fetchall()

    def get_books_by_num_group_and_disciplines(self, num_group, disciplines):
        """
        Получить книги по номеру группы и дисциплине.

        :param num_group: Номер группы.
        :param disciplines: Дисциплина.
        """
        try:
            # Выполняем запрос к базе данных для выбора книг по номеру группы и дисциплине
            self.cursor.execute("SELECT * FROM books WHERE NUM_GROUP = ? AND ID_DISCIP = ?", (num_group, disciplines))
            self.databaseConnect.commit()
        except sqlite3.Error as e:
            print("Ошибка при получении списка книг:", e)
        else:
            return self.cursor.fetchall()
    
    # library
    def get_library_value(self, num_group, student, discipline):
        """
        Получить значение книги для указанного студента и дисциплины в выбранной группе.

        :param num_group: Номер группы.
        :param student: Имя студента.
        :param discipline: Название дисциплины.
        :return: Значение книги (или None, если значение не найдено).
        """
        try:
            self.cursor.execute("SELECT BOOK FROM library WHERE NUM_GROUP = ? AND ID_STUDENT = ? AND ID_DISCIP = ?", (num_group, student, discipline))
            result = self.cursor.fetchone()
            if result:
                return result[0]  # Возвращаем значение книги из результата запроса
            else:
                return None  # Если значение не найдено, возвращаем None
        except sqlite3.Error as e:
            print("Ошибка при получении значения из таблицы library:", e)
            return None  # В случае ошибки также возвращаем None

    def update_database_value(self, num_group, student, discipline, value):
        """
        Получить значение книги для указанного студента и дисциплины в выбранной группе.

        :param num_group: Номер группы.
        :param student: Имя студента.
        :param discipline: Название дисциплины.
        :return: Значение книги (или None, если значение не найдено).
        """
        try:
            self.cursor.execute("SELECT * FROM library WHERE NUM_GROUP=? AND ID_STUDENT=? AND ID_DISCIP=?", (num_group, student, discipline))
            existing_record = self.cursor.fetchone()

            if existing_record:
                # Запись существует, обновляем значение
                self.cursor.execute("UPDATE library SET BOOK=? WHERE NUM_GROUP=? AND ID_STUDENT=? AND ID_DISCIP=?", (value, num_group, student, discipline))
            else:
                # Запись не существует, создаем новую запись
                self.cursor.execute("INSERT INTO library (NUM_GROUP, ID_STUDENT, ID_DISCIP, BOOK) VALUES (?, ?, ?, ?)", (num_group, student, discipline, value))

            self.databaseConnect.commit()
        except sqlite3.Error as error:
            print("Ошибка при работе с базой данных:", error)
            return False  # Возврат информации об ошибке