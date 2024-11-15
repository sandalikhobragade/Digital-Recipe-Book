from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    preparation_time = models.PositiveIntegerField(help_text="Time in minutes")
    meal_type = models.CharField(max_length=50, choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')])
    image = models.ImageField(upload_to='recipe_images/', null=True, blank=True)
    
    def __str__(self):
        return self.name

