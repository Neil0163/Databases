# 2) import 1 relvent 
from lib.book import Books

# 1) Create test for model class, use the seeds to see what will be in the model
#       in this case id, title, author_name
#       create an instance of a book and lable it with relventa
def test_for_model():
    book = Books(1, "Three Little Pigs", "J. Jacobs")
    assert book.id ==1
    assert book.title == "Three Little Pigs"
    assert book.author_name == "J. Jacobs"




# 4) Create a test for equality (two the same)
#    book1 = Books(insert relvent)
#    repeate above naming different 
#    assert 
def test_for_eq():
    book1 = Books(1, "Three Little Pigs", "J. Jacobs")
    book2 = Books(1, "Three Little Pigs", "J. Jacobs")
    assert book1 == book2 



# 3) create a test for format ensuring the assert is converted to string 
#       book = Books(insert relevent)
#       assert type(call) == (insert result)
def test_for_formatting():
    book = Books(1, "Three Little Pigs", "J. Jacobs")
    assert str(book) == "Books(1, Three Little Pigs, J. Jacobs)"
