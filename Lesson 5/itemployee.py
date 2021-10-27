from employee import Employee


class ITEmployee(Employee):
    """A class to represent an IT employee"""

    def __init__(self, *args, **kwargs):
        """Constructs all the necessary attributes for the IT employee object"""
        super().__init__(*args, **kwargs)
        self.skills = []

    def __str__(self):
        """Print the object"""
        return f"Full name: {self.full_name}, Year of Birth: {self.year_of_birth}, position: {self.position}, " \
               f"experience: {self.experience}, salary: {self.salary}, skills: {self.skills}"

    def add_skill(self, skill):
        """Accepts a new skill and appends it to the skills list"""
        self.skills.append(skill)
        return self.skills


it1 = ITEmployee("Boris Johnson", 1955, "Python developer", 7, 4000)
print(it1.get_name())
print(it1.get_surname())
print(it1.get_position())
print(it1.increase_salary(250))
print(it1.add_skill("German"))
print(it1.__str__())

