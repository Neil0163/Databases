# 2) import 1 relvent 
from lib.album import Album 


# 1) Create test for model class, use the seeds to see what will be in the model
#       in this case id, title, release_year, artist_id
def test_for_model_creation():
    album = Album (1, "Dark Side", 1995, 2)
    assert album.id == 1
    assert album.title == "Dark Side"
    assert album.release_year == 1995
    assert album.artist_id == 2 
    
# 3) Create a test for equality
def test_for_equality():
    album1 = Album (1, "Dark Side", 1995, 2)
    album2 = Album (1, "Dark Side", 1995, 2)
    assert album1 == album2
        
# 4) Create a test for format (how the contents is displayed) 
def test_albums_format_nicely():
    album = Album(1, "Dark Side", 1995, 2)
    assert str(album) == "Album(1, Dark Side, 1995, 2)"