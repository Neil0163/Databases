# file: app.py
#import both repositories and the database connection
from lib import album_repository
from lib import artist_repository
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.database_connection import DatabaseConnection
# Create the Class for application
# initiate self 
# create a self connection for DatabseConnection, call connect, then seed the appropriete SQL file
# apply self.artist repo and album repo to appropriete repos then pass sel._connection as argument 
class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")
        self.artist_repository = ArtistRepository(self._connection)
        self.album_repository = AlbumRepository(self._connection)

    def run(self): 
    # Greet the user using a print statment
        print("****WELCOME TO THE MUISC MANAGER***")
    #Create a while loop this will keep looping the program until a break is called.
        while True:
            #Prompt the user for an input by asking what they would like to do
            select = input("Please choose what you want to do:\n1. -List all Albums\n2. -List all Artists\n")
            #Create an if statement which does the above mentioned based on a users input
            if select == '1':
                #call the method to list all
                albums = self.album_repository.all()
                #create a for loop to itterate through albums
                for album in albums:
                    #print the result
                    print(f"{album.id}: {album.title} ({album.release_year})")
                #break out the loop
                break
            elif select == '2':
                artists = self.artist_repository.all()
                for artist in artists:
                    print(f"{artist.id}: {artist.name} ({artist.genre})")
                break
            #if the user inputs an incorrect number prompt them again until they choose a correct number
            else:
                print("Invalid selection, please select 1 or 2")
            continue

if __name__ == '__main__':
    app = Application()
    app.run()