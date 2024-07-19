from django.db import models
from authentication.models import CustomUser

class Category(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)

    def __str__(self):
        return f"{self.name}"
    

class Task(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=254, null=False)
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="task_category")

    def __Str__(self):
        return f"{self.name}"
    
    