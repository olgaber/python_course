"""Создаём наборы CRUD (create, read, update, delete) тестов (как позитивные, так
и негативные) для тестирования нашего REST API. Проверяем статус код и тело
ответа.
Не забываем про негативные тесты! Примеры: создание персонажа на книгу,
которой нет, неправильный набор свойств книг и персонажа, не правильный
тип данных."""

import unittest
import requests


class RestApiTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://pulse-rest-testing.herokuapp.com/"
        self.book = {"title": "Three in a boat", "author": "J.K. Jerome"}
        self.updated_book = {"title": "Airport", "author": "Arthur Hailey"}
        self.role = {"name": "Ron", "type": "Lead actor", "level": "2", "book": "1"}
        self.role1 = {"name": "Harry", "type": "Lead actor", "level": "1", "book": "987456"}

    def test_a_create_book(self):
        response = requests.post(self.base_url + "books", data=self.book)
        self.assertEqual(response.status_code, 201)
        resp_book = response.json()
        self.book["id"] = resp_book["id"]
        with open("new.txt", 'w') as f:
            f.write(str(self.book["id"]))
        self.assertDictEqual(self.book, resp_book)

    def test_b_get_book(self):
        with open("new.txt", 'r') as f:
            id1 = f.read()
        response = requests.get('{}books/{}/'.format(self.base_url, id1))
        self.assertEqual(response.status_code, 200)

    def test_c_update_book(self):
        with open("new.txt", 'r') as f:
            id1 = f.read()
        response = requests.put('{}books/{}/'.format(self.base_url, id1), data=self.updated_book)
        self.assertEqual(response.status_code, 200)
        with self.assertRaises(AssertionError):
            self.assertDictEqual(self.book, self.updated_book)

    def test_d_create_role(self):
        response = requests.post(self.base_url + "roles", data=self.role)
        self.assertEqual(response.status_code, 201)

    def test_e_create_role_non_existing_book(self):
        response = requests.post(self.base_url + "roles", data=self.role1)
        with self.assertRaises(AssertionError):
            self.assertEqual(response.status_code, 201)

    def test_f_delete_book(self):
        with open("new.txt", 'r') as f:
            id1 = f.read()
        response = requests.delete('{}books/{}/'.format(self.base_url, id1))
        self.assertEqual(response.status_code, 204)


if __name__ == "__main__":
    unittest.main()

