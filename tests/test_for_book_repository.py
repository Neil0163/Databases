#2) import the 2 relevant lib 
from lib.book import Books
from lib.book_respository import BookRepository

#1) create a test for a method that returns all the books when said method is called 
#   Make sure you use db_connection as an argument to connect to the database
#   seed it with the correct seed for eg db_connection.seed("seeds/<seed_file.sql>")
#   create a repository = YOUR REPOSITORY(db_connection)
#   call the method "book" and set it to repo.method
#   assert result using the input from the seed (list of books)
def test_for_return_all_books(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepository(db_connection)
    result = repository.all()
    assert result == [
        Books(1,'Nineteen Eighty-Four', 'George Orwell'),
        Books(2,'Mrs Dalloway', 'Virginia Woolf'),
        Books(3,'Emma', 'Jane Austen'),
        Books(4,'Dracula', 'Bram Stoker'),
        Books(5,'The Age of Innocence', 'Edith Wharton'),
    ]







