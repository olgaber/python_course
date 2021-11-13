"""Тестируем фильтры:
- сначала просто научитесь делать эти запросы;
- потом тоже встраиваем в тесты.
В нашем тестовом REST приложении уже реализованы фильтры для roles.
Вы можете получать частичный список ролей, фильтруя по book_id, type и level,
передавая их в качестве параметра."""

import unittest
import requests


class FilterTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://pulse-rest-testing.herokuapp.com/"
        self.exist_book_id = 1
        self.type = "Wizard"
        self.level = "level__gte"
        self.number = 3

    def test_a_get_roles_by_id(self):
        response = requests.get(f"{self.base_url}roles/?book_id={self.exist_book_id}")
        print("Roles by book id:\n" + str(response.json()))
        self.assertEqual(response.status_code, 200, "Code should be 200")

    def test_b_get_roles_by_type(self):
        response = requests.get(f"{self.base_url}roles/?type={self.type}")
        print("Roles by type:\n" + str(response.json()))
        self.assertEqual(response.status_code, 200, "Code should be 200")

    def test_c_get_roles_by_level1(self):
        response = requests.get(f"{self.base_url}roles/?level={self.number}")
        print("Roles by level:\n" + str(response.json()))
        self.assertEqual(response.status_code, 200, "Code should be 200")

    def test_d_get_roles_by_level2(self):
        response = requests.get(f"{self.base_url}roles/?{self.level}={100400}")
        print("Roles greater than or equal:\n" + str(response.json()))
        self.assertEqual(response.status_code, 200, "Code should be 200")

    def test_e_get_roles_combined(self):
        response = requests.get(f"{self.base_url}roles/?{self.level}={1}&type={self.type}"
                                f"&book_id={self.exist_book_id}")
        print("Roles with combined filters:\n" + str(response.json()))
        self.assertEqual(response.status_code, 200, "Code should be 200")


if __name__ == "__main__":
    unittest.main()

