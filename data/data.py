# File data.py

import sqlite3
from datetime import datetime

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
            \"DISCIPLINES\" TEXT NOT NULL,\
            \"NAME\"  TEXT NOT NULL,\
            \"AUTHOR\" TEXT NOT NULL,\
            \"PUBLISHER\" TEXT NOT NULL,\
            \"YEAR_PUB\" INTEGER NOT NULL,\
            \"YEAR_LICENSE_EXP\" INTEGER NOT NULL)")
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
            \"STUDENTS\"    TEXT NOT NULL,\
            \"DISCIPLINES\" TEXT NOT NULL,\
            \"BOOK\" TEXT NOT NULL,\
            \"DATE\" TEXT NOT NULL)")
        self.databaseConnect.commit()

    # group
    def create_group(self, num_group):
        try:
            self.cursor.execute("SELECT * FROM groups WHERE NUM_GROUP=?", (num_group,))
            group_exists = self.cursor.fetchone()

            if group_exists:
                print(f"Группа с номером {num_group} уже существует в базе данных.")
            else:
                self.cursor.execute("INSERT INTO groups (NUM_GROUP) VALUES (?)", (num_group,))
                self.databaseConnect.commit()
                print(f"Группа с номером {num_group} успешно добавлена в базу данных.")
        except sqlite3.Error as e:
            print("Ошибка при добавлении группы в базу данных:", e)


    def delete_group(self, num_group):
        try:
            self.cursor.execute("DELETE FROM library WHERE NUM_GROUP = ?", (num_group,))
            self.cursor.execute("DELETE FROM disciplines WHERE NUM_GROUP = ?", (num_group,))
            self.cursor.execute("DELETE FROM students WHERE NUM_GROUP = ?", (num_group,))
            self.cursor.execute("DELETE FROM books WHERE NUM_GROUP = ?", (num_group,))
            self.databaseConnect.commit()

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
        try:
            self.cursor.execute("SELECT * FROM groups WHERE NUM_GROUP=?", (num_group,))
            group_exists = self.cursor.fetchone()

            if group_exists:
                self.cursor.execute("SELECT * FROM disciplines WHERE NUM_GROUP=? AND NAME=?", (num_group, disciplines))
                existing_discipline = self.cursor.fetchone()

                if existing_discipline:
                    print(f"Дисциплина {disciplines} уже существует для группы {num_group}.")
                else:
                    self.cursor.execute("INSERT INTO disciplines (NUM_GROUP, NAME) VALUES (?, ?)",(num_group, disciplines))
                    self.databaseConnect.commit()
                    print(f"Дисциплина {disciplines} группы {num_group} успешно добавлена в базу данных.")
            else:
                print(f"Группы с номером {num_group} не существует в базе данных. Создаем новую группу...")
                self.create_group(num_group)

                self.cursor.execute("SELECT * FROM disciplines WHERE NUM_GROUP=? AND NAME=?", (num_group, disciplines))
                existing_discipline = self.cursor.fetchone()

                if existing_discipline:
                    print(f"Дисциплина {disciplines} уже существует для группы {num_group}.")
                else:
                    self.cursor.execute("INSERT INTO disciplines (NUM_GROUP, NAME) VALUES (?, ?)",(num_group, disciplines))
                    self.databaseConnect.commit()
                    print(f"Дисциплина {disciplines} группы {num_group} успешно добавлена в базу данных.")

        except sqlite3.Error as e:
            print("Ошибка при добавлении дисциплин:", e)


    def delete_disciplines(self, num_group, disciplines):
        try:
            self.cursor.execute("DELETE FROM library WHERE DISCIPLINES IN (SELECT ID FROM disciplines WHERE NAME = ? AND NUM_GROUP = ?)", (disciplines, num_group))
            self.databaseConnect.commit()

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
    def create_students(self, num_group, student):
        try:
            self.cursor.execute("SELECT * FROM groups WHERE NUM_GROUP=?", (num_group,))
            group_exists = self.cursor.fetchone()

            if group_exists:
                self.cursor.execute("SELECT * FROM students WHERE NUM_GROUP=? AND NAME=?", (num_group, student))
                existing_student = self.cursor.fetchone()

                if existing_student:
                    print(f"Студент {student} уже существует в группе {num_group}.")
                else:
                    self.cursor.execute("INSERT INTO students (NUM_GROUP, NAME) VALUES (?, ?)",(num_group, student))
                    self.databaseConnect.commit()
                    print(f"Студент {student} группы {num_group} успешно добавлен в базу данных.")
            else:
                print(f"Группы с номером {num_group} не существует в базе данных. Создаем новую группу...")
                self.create_group(num_group)

                self.cursor.execute("SELECT * FROM students WHERE NUM_GROUP=? AND NAME=?", (num_group, student))
                existing_student = self.cursor.fetchone()

                if existing_student:
                    print(f"Студент {student} уже существует в группе {num_group}.")
                else:
                    self.cursor.execute("INSERT INTO students (NUM_GROUP, NAME) VALUES (?, ?)",(num_group, student))
                    self.databaseConnect.commit()
                    print(f"Студент {student} группы {num_group} успешно добавлен в базу данных.")
        except sqlite3.Error as e:
            print("Ошибка при добавлении студента:", e)


    def delete_students(self, num_group, students):
        try:
            
            self.cursor.execute("DELETE FROM library WHERE DISCIPLINES IN (SELECT ID FROM students WHERE NAME = ? AND NUM_GROUP = ?)", (students, num_group))
            self.databaseConnect.commit()
            
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
    def create_books(self, num_group, disciplines, books, author, publisher, year_pub, year_license_exp):
        try:
            self.cursor.execute("SELECT * FROM groups WHERE NUM_GROUP=?", (num_group,))
            group_exists = self.cursor.fetchone()

            if group_exists:
                self.cursor.execute("SELECT * FROM disciplines WHERE NUM_GROUP=? AND NAME=?", (num_group, disciplines))
                discipline_exists = self.cursor.fetchone()

                if discipline_exists:
                    self.cursor.execute("SELECT * FROM books WHERE NUM_GROUP=? AND DISCIPLINES=? AND NAME=?", (num_group, disciplines, books))
                    existing_book = self.cursor.fetchone()

                    if existing_book:
                        print(f"Книга {books} уже существует для дисциплины {disciplines} и группы {num_group}.")
                    else:
                        self.cursor.execute("INSERT INTO books (NUM_GROUP, DISCIPLINES, NAME, AUTHOR, PUBLISHER, YEAR_PUB, YEAR_LICENSE_EXP) VALUES (?, ?, ?, ?, ?, ?, ?)",
                                        (num_group, disciplines, books, author, publisher, year_pub, year_license_exp))
                        self.databaseConnect.commit()
                        print(f"Книга {books} для дисциплины {disciplines} и группы {num_group} успешно добавлена в базу данных.")
                else:
                    print(f"Дисциплины {disciplines} не существует для группы {num_group}. Создаем новую дисциплину...")
                    self.create_disciplines(num_group, disciplines)

                    self.cursor.execute("INSERT INTO books (NUM_GROUP, DISCIPLINES, NAME, AUTHOR, PUBLISHER, YEAR_PUB, YEAR_LICENSE_EXP) VALUES (?, ?, ?, ?, ?, ?, ?)",
                                        (num_group, disciplines, books, author, publisher, year_pub, year_license_exp))
                    self.databaseConnect.commit()
                    print(f"Книга {books} для дисциплины {disciplines} и группы {num_group} успешно добавлена в базу данных.")
            else:
                print(f"Группы с номером {num_group} не существует в базе данных. Создаем новую группу...")
                self.create_group(num_group)

                print(f"Дисциплины {disciplines} не существует для группы {num_group}. Создаем новую дисциплину...")
                self.create_disciplines(num_group, disciplines)

                self.cursor.execute("INSERT INTO books (NUM_GROUP, DISCIPLINES, NAME, AUTHOR, PUBLISHER, YEAR_PUB, YEAR_LICENSE_EXP) VALUES (?, ?, ?, ?, ?, ?, ?)",
                                        (num_group, disciplines, books, author, publisher, year_pub, year_license_exp))
                self.databaseConnect.commit()
                print(f"Книга {books} для дисциплины {disciplines} и группы {num_group} успешно добавлена в базу данных.")
        except sqlite3.Error as e:
            print("Ошибка при добавлении книг:", e)

    
    def delete_books(self, num_group, disciplines, books):
        try:
            self.cursor.execute("DELETE FROM library WHERE NUM_GROUP = ? AND DISCIPLINES = ? AND BOOK = ?", (num_group, disciplines, books))
            self.databaseConnect.commit()
            print(f"Связанные записи в таблице library для книги {books} успешно удалены.")
            
            self.cursor.execute("DELETE FROM books WHERE NUM_GROUP = ? AND DISCIPLINES = ? AND NAME = ?", (num_group, disciplines, books))
            self.databaseConnect.commit()
            print(f"Книга {books} для группы {num_group} и дисциплины {disciplines} успешно удалена из базы данных.")
            
        except sqlite3.Error as e:
            print("Ошибка при удалении книги:", e)

    def get_books(self):
        try:
            self.cursor.execute("SELECT * FROM books")
            self.databaseConnect.commit()
        except sqlite3.Error as e:
            print("Ошибка при получении списка книг:", e)
        else:
            return self.cursor.fetchall()

    def get_books_by_num_group_and_disciplines(self, num_group, disciplines):
        try:            
            self.cursor.execute("SELECT * FROM books WHERE NUM_GROUP = ? AND DISCIPLINES = ?", (num_group, disciplines))
            self.databaseConnect.commit()
        except sqlite3.Error as e:
            print("Ошибка при получении списка книг:", e)
        else:
            return self.cursor.fetchall()
    
    # library
    def get_library_value(self, num_group, student, discipline):
        try:
            self.cursor.execute("SELECT BOOK FROM library WHERE NUM_GROUP = ? AND STUDENTS = ? AND DISCIPLINES = ?", (num_group, student, discipline))
            result = self.cursor.fetchone()
            if result:
                return result[0]
            else:
                return None
        except sqlite3.Error as e:
            print("Ошибка при получении значения из таблицы library:", e)
            return None  

    def update_database_value(self, num_group, student, discipline, value):
        try:
            current_date = int(datetime.now().timestamp())
            self.cursor.execute("SELECT * FROM library WHERE NUM_GROUP=? AND STUDENTS=? AND DISCIPLINES=?", (num_group, student, discipline))
            existing_record = self.cursor.fetchone()

            if existing_record:
                self.cursor.execute("UPDATE library SET BOOK=?, DATE=? WHERE NUM_GROUP=? AND STUDENTS=? AND DISCIPLINES=?", 
                                    (value, current_date, num_group, student, discipline))
            else:
                self.cursor.execute("INSERT INTO library (NUM_GROUP, STUDENTS, DISCIPLINES, BOOK, DATE) VALUES (?, ?, ?, ?, ?)", 
                                    (num_group, student, discipline, value, current_date))

            self.databaseConnect.commit()
        except sqlite3.Error as error:
            print("Ошибка при работе с базой данных:", error)
            return False
    