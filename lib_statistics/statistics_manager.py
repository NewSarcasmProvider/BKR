from data.data import DatabaseManager

class StatisticsManager:
    def __init__(self):
        self.database = DatabaseManager()

    def calculate_student_statistics(self, group_num):
        students = self.database.get_students_by_num_group(group_num)
        disciplines = self.database.get_disciplines_by_num_group(group_num)
        student_statistics = []

        for student in students:
            student_name = student[2]
            issued_books_count = sum(1 for discipline in disciplines 
                                     if self.database.get_library_value(group_num, student_name, discipline[2]) not in (None, "не выдана"))
            total_disciplines_count = len(disciplines)
            percentage = (issued_books_count / total_disciplines_count) * 100 if total_disciplines_count > 0 else 0
            student_statistics.append((student_name, percentage))
        
        return student_statistics

    def calculate_group_statistics(self):
        groups = self.database.get_groups()
        group_statistics = []

        for group in groups:
            group_num = group[1]
            students = self.database.get_students_by_num_group(group_num)
            disciplines = self.database.get_disciplines_by_num_group(group_num)
            
            total_books = len(students) * len(disciplines)
            issued_books = sum(1 for student in students for discipline in disciplines 
                               if self.database.get_library_value(group_num, student[2], discipline[2]) not in (None, "не выдана"))
            percentage = (issued_books / total_books) * 100 if total_books > 0 else 0
            group_statistics.append((group_num, percentage))
        
        return group_statistics
