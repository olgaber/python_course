# 2) Студент (свойства: имя-фамилия, специальность, год начала обучения, список
# оценок – при создании объекта, по умолчанию, пустой список).
# Методы:
# 3. Добавить новую оценку в свойство списка оценок
# 4. Посчитать средний балл,
# 5. Посчитать сколько лет учится уже студент.
from datetime import datetime


class Student:
    """A class to represent a student"""
    def __init__(self, full_name, speciality, start_year):
        self.full_name = full_name
        self.speciality = speciality
        self.start_year = start_year
        self.grades = []

    current_year = datetime.now().year

    def __str__(self):
        """Print the object"""
        return f"Student name: {self.full_name}, Speciality: {self.speciality}, " \
               f"Started education in {self.start_year}"

    def add_grade(self, new_grade):
        """Accepts new grade and adds it to grades list, returns grades list"""
        self.grades.append(new_grade)
        return self.grades

    def calculate_avg_score(self):
        """Calculates and returns average score of grades list"""
        return sum(self.grades) / len(self.grades)

    def calculate_study_period(self):
        """Calculates and returns the length of education"""
        return self.current_year - self.start_year


s1 = Student("Max Litvinov", "Programmer", 2019)
print(s1.__str__())
s1.add_grade(12)
s1.add_grade(10)
s1.add_grade(7)
s1.add_grade(9)
print(s1.grades)
print(s1.calculate_avg_score())
print(s1.calculate_study_period())


