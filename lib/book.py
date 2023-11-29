# 1) Create a book class 
#    initialise with all attributes for eg __init__ id, name etc
class Books:
    def __init__(self, id, title, author_name):
        self.id = id 
        self.title = title 
        self.author_name = author_name

# 2) Create  return repr to make format look nicer using f string and calling relvent eg id, name etc
    def __repr__(self):
        return f"Books({self.id}, {self.title}, {self.author_name})"
        

# 3) Create method for equality ensuring to return self. dict and other. dict
    def __eq__(self, other):
        return self.__dict__ == other.__dict__






