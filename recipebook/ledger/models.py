from django.db import models
from django.urls import reverse

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:ingredient', args=[str(self.id)])

class Recipe(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipes', args=[str(self.id)])

class RecipeIngredient(models.Model):
    Quantity = models.CharField(max_length=50)
    Ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name = 'ingredient')
    Recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name= 'recipe')

    def __str__(self):
        return f"{self.Quantity} of {self.Ingredient.name} in {self.Recipe.name}" 