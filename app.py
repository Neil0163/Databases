from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.recipe_respository import RecipeRepository
from lib.book_respository import BookRepository

# Connect to the database
connection = DatabaseConnection()
connection.connect()
# Seed with some seed data
connection.seed("seeds/book_store.sql") #<<<<< insert seed file here 

# Retrieve all artists
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()

# List them out
for artist in artists:
   print(artist)

#1) create an album repository, then import 
album_repository = AlbumRepository(connection)
album = album_repository.all()

#2) List albums 
for album in album:
   print(album)
   
print(album_repository.find(2))

#3 create book repository then import
book_repository = BookRepository(connection)
book = book_repository.all()

for book in book:
   print(book)

recipe_repositroy = RecipeRepository(connection)
recipe = recipe_repositroy.all()
for recipe in recipe:
   print(recipe)

print(recipe_repositroy.find(2))
