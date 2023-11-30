# 3) Import relevant class
from lib.album import Album

# 1) create a class for AlbumRepository
#   Use connection in the argument and set it to an instance variable 
#   test should fail as no all method
class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection

# 2) Create all method, this will use SQL
#       create rows with connection.execute and pass SQL "SELECT * FROM albums"
#       create ablums empty list 
#       create for loop for album = Album with row set up eg album = Album(row[id], etc etc etc)
#       append to album 

    def all(self):
        rows = self._connection.execute("SELECT * FROM albums")
        albums = [] 
        for row in rows:
            album =Album (row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(album)
        return albums
    
    def find(self, album_id):
        rows = self._connection.execute("SELECT * FROM albums WHERE id = %s",[album_id]) 
        row =rows [0]
        return Album (row["id"], row["title"], row["release_year"], row["artist_id"])
        