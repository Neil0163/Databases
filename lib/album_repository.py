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
    
#   
#4) Create a find method passing arguments refered to place holder in sql
#   create sql execution includinjg place holder 
#   create empty list pass first index
    #return the result ensure to include "row" 
#       
    def find(self, album_id):
        rows = self._connection.execute("SELECT * FROM albums WHERE id = %s",[album_id]) 
        row =rows [0]
        return Album (row["id"], row["title"], row["release_year"], row["artist_id"])
      
# 5) Create a method for create 
#    def the method and pass relvant arguments 
#    write code to execute sql (no variable needed to be set)
#    INSERT INTO (place to insert to) (colums to be updated) VALUES (relvant amount of placeholders)
#    [List of relvant colums to be updated]
#    return none   
    def create(self, album):
        self._connection.execute(
            "INSERT INTO albums (title, release_year, artist_id) VALUES (%s,%s,%s)",
            [album.title, album.release_year, album.artist_id])
        return None 
        
# Create method for delete 
# def the method and pass relvant arguments
# write code to execute sql (no variable needed to be set)
#    DELETE FROM (place to delete from ) WHERE id = placeholder",
#    [relvent]
#  return none  
    def delete(self, album):
        self._connection.execute(
            "DELETE FROM albums WHERE id = %s",
            [album]
        )
        return None
        
    
        

    
        
        