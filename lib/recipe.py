# 1) Create the class and pass it, re-run pytest it should get a little further
# 2) Create the init statement, re-run pytest, it should pass
# 3) Create method for eq (checks to see that despite two artist being the same there seen as seperate instances)
#4) Create method for Repr in f string format

class Recipe:
    def __init__ (self,id,name,cooking_time_minutes,rating):
        self.id = id
        self.name = name
        self.cooking_time_minutes = cooking_time_minutes
        self.rating = rating
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__ 
        
    def __repr__(self):
        return f"Recipe({self.id}, {self.name}, {self.cooking_time_minutes}, {self.rating})"
    
    