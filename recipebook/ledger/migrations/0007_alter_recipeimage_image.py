# Generated by Django 5.1.6 on 2025-03-29 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0006_alter_recipeimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='recipe_images/'),
        ),
    ]
