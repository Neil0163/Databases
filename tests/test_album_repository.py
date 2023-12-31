#2) Import the relvenat 
from lib.album_repository import AlbumRepository
from lib.album import Album

#1) create a test for a method that returns all the albums when said method is called 
#   Make sure you use db_connection as an argument to connect to the database and seed it with the correct seed
#   create an approprite repository
#   call the method 
#   assert result 
def test_for_all_method(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    result = repository.all()
    assert result == [
        Album(1,'Doolittle', 1989, 1),
        Album(2,'Surfer Rosa', 1988, 1),
        Album(3,'Waterloo', 1974, 2),
        Album(4,'Super Trouper', 1980, 2),
        Album(5,'Bossanova', 1990, 1),
        Album(6,'Lover', 2019, 3),
        Album(7,'Folklore', 2020, 3),
        Album(8,'I Put a Spell on You', 1965, 4),
        Album(9,'Baltimore', 1978, 4),
        Album(10,'Here Comes the Sun', 1971, 4),
        Album(11,'Fodder on My Wings', 1982, 4),
        Album(12,'Ring Ring', 1973, 2)
    ]
# Create a test for find method
#   First, create def function and pass argument for connection (db_connection)
#   seed the db_connection with the relvent sql file
#   create a new repository ensuring to pass the db_connection into the argument 
#   create a result variable and set the method being tested to it
#   assert result with expected output 
def test_for_find(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    result = repository.find(3)
    assert result == Album(3,'Waterloo', 1974, 2) 
    
# Create a test for create method
#   First, create def function and pass argument for connection (db_connection)
#   seed the db_connection with the relvent sql file
#   create a new repository and call the repository ensuring to pass the db_connection into the argument
#   create new variable and set it to relevent in this case album = albums (etc, etc ,etc)
#   assert the repository.(testing method)(above var) == none
#   assert the result to expected output by calling the all method, add the output to the table
def test_for_create_method(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    album = Album(None, "title", 2002, 2)
    assert repository.create(album) == None
    result = repository.all()
    assert result == [
        Album(1,'Doolittle', 1989, 1),
        Album(2,'Surfer Rosa', 1988, 1),
        Album(3,'Waterloo', 1974, 2),
        Album(4,'Super Trouper', 1980, 2),
        Album(5,'Bossanova', 1990, 1),
        Album(6,'Lover', 2019, 3),
        Album(7,'Folklore', 2020, 3),
        Album(8,'I Put a Spell on You', 1965, 4),
        Album(9,'Baltimore', 1978, 4),
        Album(10,'Here Comes the Sun', 1971, 4),
        Album(11,'Fodder on My Wings', 1982, 4),
        Album(12,'Ring Ring', 1973, 2),
        Album(13, "title", 2002, 2)
    ]

# Create a test for delete method 
# First, create def function and pass argument for connection (db_connection)
#  seed the db_connection with the relvent sql file
# assert call the method to test repo.(method) and pass the relvant id to delete asserted as none 
# create a result var and set it to the method that list all

def test_for_delete_method(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    assert repository.delete(3) == None 
    result = repository.all()
    assert result == [
        Album(1,'Doolittle', 1989, 1),
        Album(2,'Surfer Rosa', 1988, 1),
        Album(4,'Super Trouper', 1980, 2),
        Album(5,'Bossanova', 1990, 1),
        Album(6,'Lover', 2019, 3),
        Album(7,'Folklore', 2020, 3),
        Album(8,'I Put a Spell on You', 1965, 4),
        Album(9,'Baltimore', 1978, 4),
        Album(10,'Here Comes the Sun', 1971, 4),
        Album(11,'Fodder on My Wings', 1982, 4),
        Album(12,'Ring Ring', 1973, 2)
    ] 





