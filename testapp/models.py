from django.db import models


# Create your models here.
class TestModel(models.Model):
    title = models.TextField()
    description = models.CharField(max_length=1000)


class NewModel(models.Model):
    val1 = models.TextField()

    def __str__(self):
        return self.val1
