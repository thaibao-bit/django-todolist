from django.contrib import admin
from .models import TestModel, NewModel

# Register your models here.
admin.site.register(TestModel)
admin.site.register(NewModel)