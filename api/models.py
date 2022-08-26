from django.db import models

class Recipe(models.Model):
    name_recipe = models.CharField(max_length=100)
    favorite = models.BooleanField()
    recipe_owner = models.CharField(max_length=80)
    color_card = models.CharField(max_length=6)