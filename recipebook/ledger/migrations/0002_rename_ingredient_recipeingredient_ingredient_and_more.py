# Generated by Django 5.1.6 on 2025-03-06 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipeingredient',
            old_name='ingredient',
            new_name='Ingredient',
        ),
        migrations.RenameField(
            model_name='recipeingredient',
            old_name='quantity',
            new_name='Quantity',
        ),
        migrations.RenameField(
            model_name='recipeingredient',
            old_name='recipe',
            new_name='Recipe',
        ),
    ]
