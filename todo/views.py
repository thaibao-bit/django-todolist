from django.shortcuts import render, redirect
from .models import ToDoModel

# Create your views here.


def todo_view(request, *args, **kwargs):

    tod = ToDoModel.objects.all()
    if request.method == 'POST':
        new_model = ToDoModel(
            title=request.POST['title']
        )
        new_model.save()
        return redirect('/')

    return render(request, "todo.html", {'todos': tod})


def delete(request, d):
    tod = ToDoModel.objects.get(id=d)
    tod.delete()
    return redirect('/')
