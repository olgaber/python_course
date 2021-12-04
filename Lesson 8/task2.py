"""
    • Перепишите ваши тесты на Pytest. Как вам удобно или заново написать, или переделать тесты с unittest
    • Советую использовать pytest.fixture, а не setup и teardown. Хотя можно объединять, если вам захочется
    использовать классы.
    • Параметризуем тесты данными
    • * (для продвинутых) считайте данные из файла файла (можно в json формате)
    • * (для еще более продвинутых) попробуйте всё-таки http.client
"""
import requests


# Create a book
def test_create_book(base_url):
    response = requests.post(f"{base_url}/books",
                             data={"title": "Da Vinci Code", "author": "Dan Brown"})
    new_book = response.json()
    assert response.status_code == 201, "Book isn't created"
    requests.delete(f"{base_url}/books/{new_book['id']}")


# Read a book
def test_get_book(base_url, create_delete_book):
    book = create_delete_book
    response = requests.get(f"{base_url}/books/{book['id']}/")
    assert response.status_code == 200, "Book doesn't exist"


# Search in the list
def test_search_in_list(base_url, create_delete_book):
    book = create_delete_book
    response = requests.get(f"{base_url}/books")
    ls = response.json()
    """Finds a book by id. Receives list of json objects, searches for the specified id"""
    counter = 0
    for el in ls:
        for key in el:
            if book["id"] == el[key]:
                counter += 1
    assert counter == 1, "Book isn't found in the list"


# # Update a book
# def test_update_book():
#     pass
#

#
# # Delete a book
# def test_delete_book():
#     pass