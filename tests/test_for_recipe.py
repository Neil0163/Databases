# 2) import 1 relvent 
from lib.recipe import Recipe
# 1) Create test for model class, use the seeds to see what will be in the model
#       in this case id, name, cooking_time, rating
def test_for_model_class():
    recipe = Recipe(1, "Chilli", 22, 3)
    assert recipe.id ==1
    assert recipe.name == "Chilli"
    assert recipe.cooking_time_minutes == 22
    assert recipe.rating == 3 


# 4) Create a test for equality
def test_for_eq():
    recipe1 = Recipe(1, "Chilli", 22, 3)
    recipe2 = Recipe(1, "Chilli", 22, 3)
    assert recipe1 == recipe2
    
# 3) Create a test for format
def test_for_foramtting():
    recipe = Recipe(1, "Chilli", 22, 3)
    assert str(recipe) == "Recipe(1, Chilli, 22, 3)"