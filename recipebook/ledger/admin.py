from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient, Profile, RecipeImage
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ('name', )
    list_display = ('name' ,)

class RecipeImageAdmin(admin.ModelAdmin):
    model = RecipeImage
    list_display = ('recipe', 'image', 'description')  

class RecipeImageInline(admin.TabularInline):  
    model = RecipeImage
    extra = 1  

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ('name', 'author', 'created_on', 'updated_on',)
    list_display = ('name' , 'author', 'created_on', 'updated_on',)
    inlines = [RecipeImageInline]

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    search_fields = ('Quantity' , 'Ingredient', 'Recipe' )
    list_display = ('Quantity' , 'Ingredient', 'Recipe'  )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(RecipeImage, RecipeImageAdmin)
