from employee import Employee
import unittest


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


class TestITEmployee(unittest.TestCase):

    def setUp(self):
        self.it_emp = ITEmployee("Boris Johnson", 1955, "Python developer", 7, 4000)

    def test_full_name(self):
        self.assertEqual(self.it_emp.full_name, "Boris Johnson")

    def test_year_of_birth(self):
        self.assertGreaterEqual(self.it_emp.year_of_birth, 1949)

    def test_no_skills(self):
        self.assertEqual(len(self.it_emp.skills), 0)

    def test_add_skill(self):
        self.it_emp.add_skill("German")
        self.assertIn("German", self.it_emp.skills)

