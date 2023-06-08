def find(books, author):
    for book in books:
        if author(book):
            return book
    return None
