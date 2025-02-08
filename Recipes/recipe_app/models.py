from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=250)
    instructions = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name
    
