#2) Import the 2 relvenat 
from lib.recipe_respository import RecipeRepository
from lib.recipe import Recipe
#1) create a test for a method that returns all the recipes when said method is called 
#   Make sure you use db_connection as an argument to connect to the database and seed it with the correct seed
#   create an approprite repository with db_connection
#   call the method 
#   assert result 
def test_for_all(db_connection):
    db_connection.seed("seeds/recipes.sql")
    respository = RecipeRepository(db_connection)
    result = respository.all()
    assert result == [
        Recipe(1,'Chilli', 20, 3),
        Recipe(2,'Burgers', 25, 4),
        Recipe(3,'Chicken Curry', 25, 4)]
        
    
#3) Create a test for method find
#   set up db_connection.seed wth relevant seed sql
#   create a repository named Recipe(db_connection)
#   create result to call repo.method(idnumber)
#   assert the result

def test_for_find(db_connection):
    db_connection.seed("seeds/recipes.sql")
    respository = RecipeRepository(db_connection)
    result = respository.find(2)
    assert result == Recipe(2,'Burgers', 25, 4) 