from django.shortcuts import render
from .models import Recipe, RecipeIngredient, Ingredient

# Create your views here.

def index(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, 'recipe.html', context)

def recipes(request, num = 1):
    recipe_num = Recipe.objects.get(pk = num)
    ingredients = RecipeIngredient.objects.filter(Recipe__name= recipe_num.name)
    context = { 'recipe' : recipe_num, 'ingredients' : ingredients}
    return render(request, 'recipecontent.html', context) 


