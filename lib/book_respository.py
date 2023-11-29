# 3) import 1 relvant 
from lib.book import Books


# 1) create a class for BookRepository
#   Use connection in the argument 
#   __init__self._connection
#   test should fail as no all method
class BookRepository:
    def __init__(self, connection):
        self._connection = connection



# 2) Create all method, this will use SQL
#       def all method
#       create rows with self._connection.execute and pass SQL ()"SELECT * FROM books")
#       create books empty list 
#       create for loop for rows book = Books with row set up eg Books(row[id], row[etc] row[etc] 
#       append to book
#       retrun the appropriate
    def all(self):
        rows = self._connection.execute("SELECT * FROM books")
        books = []
        for row in rows:
            book = Books(row["id"], row["title"], row["author_name"])
            books.append(book)
        return books


