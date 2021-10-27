from datetime import datetime


class Person:
    """A class to represent a person"""
    def __init__(self, full_name, year_of_birth):
        """Constructs all the necessary attributes for the person"""
        self.full_name = full_name
        self.year_of_birth = year_of_birth

    def __str__(self):
        """Print the object"""
        return f"Full name: {self.full_name}, Year of Birth: {self.year_of_birth}"

    current_year = datetime.now().year

    def get_name(self):
        """Returns first name from full name"""
        f_name = self.full_name.split(" ")
        first_name = f_name[0]
        return first_name

    def get_surname(self):
        """Returns last name from full name"""
        f_name = self.full_name.split(" ")
        last_name = f_name[1]
        return last_name

    def age_in(self, year=None):
        """
        Returns age in the year, passed as parameter.
        If the year isn't passed, returns age in the current year
        """
        if year is None:
            age = self.current_year - self.year_of_birth
        else:
            age = year - self.year_of_birth
        return age


p1 = Person("Ivan Petrov", 1950)
print(p1.__str__())
print(p1.get_name())
print(p1.get_surname())
print(p1.age_in())
print("----------------------------")

