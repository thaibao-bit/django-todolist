from django.urls import path
from . import views


urlpatterns = [
    path('', views.test_view, name="testIndex"),
    path('deletetest/<str:d>', views.delete_test, name="deleteIndex"),
]
