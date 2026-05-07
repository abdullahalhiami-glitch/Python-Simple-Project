books = {"Book_A": {"author": "Ahmed", "copies": 3}, "Book_B": {"author": "Sara", "copies": 0}}

def add_new_book(title, author, copies):
    if title in books:
        print("Book already exists.")
        return
    books[title] = {"author": author, "copies": copies}
    print(f"Book '{title}' added.")

def get_available_books():
    return {k: v for k, v in books.items() if v["copies"] > 0}

def search_by_author(author_name):
    return {k: v for k, v in books.items() if v["author"] == author_name}

def borrow_book(title):
    if title not in books:
        return "Book not found."
    if books[title]["copies"] > 0:
        books[title]["copies"] -= 1
        return "Book borrowed successfully."
    else:
        return "Book out of stock."

def return_book(title):
    if title not in books:
        return "Book not found."
    books[title]["copies"] += 1
    return "Book returned successfully."

def check_book_stock(title):
    if title not in books:
        return "Book not found."
    return books[title]["copies"]

def get_out_of_stock_books():
    return [k for k, v in books.items() if v["copies"] == 0]

def delete_book(title):
    if title in books:
        del books[title]
        return "Book deleted."
    else:
        return "Book not found."