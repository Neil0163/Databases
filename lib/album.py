# 1) Create the class and pass it, re-run pytest it should get a little further
# 2) Create the init statement, re-run pytest, it should pass

class Album:
    def __init__(self, id, title, release_year, artist_id):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id
# 3) Create method for eq (checks to see that despite two artist being the same there seen as seperate instances)
    def __eq__ (self, other):
        return self.__dict__ == other.__dict__
        
#4) Create method for Repr in f string format
    def __repr__(self):
        return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_id})"

