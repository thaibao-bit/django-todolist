from django.db import models


# Create your models here.
class ToDoModel(models.Model):
    title = models.CharField(max_length=256, default= "B")

    def __str__(self):
        return self.title
