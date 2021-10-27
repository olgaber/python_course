from person import Person


class Employee(Person):
    """A class to represent an employee"""
    def __init__(self, full_name, year_of_birth, position, experience, salary):
        super().__init__(full_name, year_of_birth)
        self.position = position
        self.experience = experience
        self.salary = salary

    def __str__(self):
        """Print the object"""
        return f"Full name: {self.full_name}, Year of Birth: {self.year_of_birth}, position: {self.position}, " \
               f"experience: {self.experience}, salary: {self.salary}"

    def get_position(self):
        """Returns position prefix according to experience"""
        if self.experience < 3:
            return f"Junior {self.position}"
        elif 3 <= self.experience < 6:
            return f"Middle {self.position}"
        else:
            return f"Senior {self.position}"

    def increase_salary(self, amount):
        """Accepts amount and increases salary with this amount"""
        self.salary += amount
        return self.salary


e1 = Employee("Peter Pen", 1980, "AQA", 5, 2500)
print(e1.__str__())
print(e1.get_name())
print(e1.get_surname())
print(e1.get_position())
print(e1.increase_salary(250))
print("----------------------------")


