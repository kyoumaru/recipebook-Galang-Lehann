from django.urls import path
from .views import index, recipes

urlpatterns = [
    path('recipes/list', index, name = 'index'),
    path('recipe/<int:num>', recipes, name = 'recipes'),
]
app_name = "ledger"

