from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe, RecipeIngredient
from .forms import RecipeForm, RecipeImageForm

# Create your views here.
# the names of the functions are changed to make it cleaner
def recipes_list(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, 'recipe.html', context)

@login_required
def recipe_detail(request, num = 1):
    recipe_num = Recipe.objects.get(pk = num)
    ingredients = RecipeIngredient.objects.filter(Recipe__name= recipe_num.name)
    context = { 'recipe' : recipe_num, 'ingredients' : ingredients}
    return render(request, 'recipe_content.html', context) 

@login_required
def recipe_add(request):
    form = RecipeForm()

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ledger:recipes_list')
        else:
            form = RecipeForm()
            
    context = {'form': form}
    return render(request, 'recipe_add.html', context)


@login_required
def image_add(request, pk):
    form = RecipeImageForm()
    recipe = Recipe.objects.get(pk=pk)

    if request.method == "POST":
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ledger:recipe_detail', pk)
        else:
            form = RecipeImageForm()
            
    context = { 'form': form,'recipe': recipe }
    return render(request, 'image_add.html', context)