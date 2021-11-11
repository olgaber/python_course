import requests


def create_book():
    """Create and returns a new book"""
    response = requests.post("http://pulse-rest-testing.herokuapp.com/books",
                             data={"title": "Call of Ktulu", "author": "Howard Lovecraft"})
    print("Create book code: " + str(response.status_code))
    assert response.status_code == 201, "Book isn't created"
    new_book = response.json()
    print("New book id: " + str(new_book["id"]))
    return new_book["id"]


def create_role():
    book_id = create_book()
    response = requests.post("http://pulse-rest-testing.herokuapp.com/roles",
                             data={"name": "Francis Wayland Thurston", "type": "Anthropologist", "level": "17",
                                   "book": book_id})
    print("Create role code: " + str(response.status_code))
    assert response.status_code == 201, "Role isn't created"
    return response.json()


def check_role_url(some_role):
    """Check if the role exists by id"""
    response = requests.get("http://pulse-rest-testing.herokuapp.com/roles/" + str(some_role["id"]))
    print("The role exists code: " + str(response.status_code))
    if response.status_code == 200:
        print("The role exists by URL!")
    else:
        print("Role doesn't exist!")


role = create_role()
check_role_url(role)

