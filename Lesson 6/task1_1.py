import requests


def create_book():
    """Create and returns a new book"""
    response = requests.post("http://pulse-rest-testing.herokuapp.com/books",
                             data={"title": "Da Vinci Code", "author": "Dan Brown"})
    print("Create book code: " + str(response.status_code))
    assert response.status_code == 201, "Book isn't created"
    new_book = response.json()
    print("New book id: " + str(new_book["id"]))
    return new_book


def check_book_url(some_book):
    """Check if the book exists by id"""
    response = requests.get("http://pulse-rest-testing.herokuapp.com/books/" + str(some_book["id"]))
    print("The book exists code: " + str(response.status_code))
    # assert response.status_code == 200, "The book doesn't exist"
    if response.status_code == 200:
        print("The book exists by URL!")
    elif response.status_code == 404:
        print("The book was deleted!")
    else:
        print("Weird situation!")


def search_in_list(some_book):
    response = requests.get("http://pulse-rest-testing.herokuapp.com/books/")
    ls = response.json()
    """Finds a book by id. Receives list of json objects, searches for the specified id"""
    for el in ls:
        for key in el:
            if el[key] == some_book["id"]:
                print("The book is found in the list!")


def update_book(some_book):
    """Updates book's title and author name by id, returns updated book"""
    response = requests.put("http://pulse-rest-testing.herokuapp.com/books/" + str(some_book["id"]),
                            data={"title": "Inferno", "author": "Brown Dan"})
    print("Update book code: " + str(response.status_code))
    assert response.status_code == 200, "The book isn't updated"
    return response.json()


def check_update_success(initial_book, upd_book):
    """Checks the changes were applied"""
    counter = 0
    for key in initial_book:
        if initial_book[key] != upd_book[key]:
            counter += 1
    if counter >= 1:
        print("The book was updated")
    else:
        print("The book wasn't updated")


def search_updated_in_list(some_book):
    response = requests.get("http://pulse-rest-testing.herokuapp.com/books/")
    ls = response.json()
    """Finds a book by id. Receives list of json objects, searches for the specified id"""
    for el in ls:
        counter = 0
        for key in el:
            if el[key] == some_book["id"]:
                counter += 1
                print("The updated book is found in the list!")
            if counter == 0:
                continue
            if el[key] == some_book["title"]:
                counter += 1
            if el[key] == some_book["author"]:
                counter += 1
        if counter == 3:
            print("The updated book is in the list")
        if 0 < counter < 3:
            print("The updated book is not in the list")
            print(counter)


def delete_book(some_book):
    """Deletes the updated book by id"""
    response = requests.delete("http://pulse-rest-testing.herokuapp.com/books/" + str(some_book["id"]))
    print("Delete book code: " + str(response.status_code))
    assert response.status_code == 204, "The book isn't deleted"


# create new book
book = create_book()

# check by id that the book is created
check_book_url(book)

# check the new book is available in the list
search_in_list(book)

# update book and save it to dictionary
updated_book = update_book(book)

# check by id that the updated book exists
check_book_url(updated_book)

# check the book was updated
check_update_success(book, updated_book)

# check the updated book is available in the list
search_updated_in_list(updated_book)

# delete the updated book
delete_book(updated_book)

# check the updated book was deleted
check_book_url(updated_book)

