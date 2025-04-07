from django.urls import path
from .views import recipes_list, recipe_detail, recipe_add, image_add
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('recipes/list', recipes_list, name = 'recipes_list'),
    path('recipe/<int:num>', recipe_detail, name = 'recipe_detail'),
    path('recipe/add/', recipe_add, name='recipe_add'),
    path('recipe/<int:pk>/add_image/', image_add, name='image_add'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
app_name = "ledger"
