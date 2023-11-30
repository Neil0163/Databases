# 3) Import relevant class
from lib.recipe import Recipe
# 1) create a class for RecipeRepository
#    initiate and Use connection in the argument and set it to an instance variable 
#   test should fail as no all method
class RecipeRepository:
    def __init__(self, connection):
        self._connection = connection
# 2) Create all method, this will use SQL
#       create rows with intiaitlise  connection.execute and pass SQL "SELECT * FROM albums"
#       create ablums empty list 
#       create for loop for album = Album with row set up eg album = Album(row[id], etc etc etc)
#       append to album 
    def all(self):
        rows = self._connection.execute("SELECT * FROM recipes")
        recipes = []
        for row in rows:
            recipe = Recipe(row["id"], row["name"], row["cooking_time_minutes"], row["rating"])
            recipes.append(recipe)
        return recipes
        
#4) Create a find method passing arguments refered to place holder in sql
#   create sql execution includinjg place holder 
#   create empty list pass first index
    #return the result ensure to include "row" 
    def find(self, rating):
        rows = self._connection.execute("SELECT * FROM recipes WHERE id = %s", [rating])
        row = rows [0]
        return Recipe(row["id"], row["name"], row["cooking_time_minutes"], row["rating"]) 
        