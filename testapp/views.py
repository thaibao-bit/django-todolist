from django.shortcuts import render,redirect
from .models import TestModel, NewModel


# Create your views here.
def test_view(request, *args, **kwargs):
    testM = TestModel.objects.all()
    newM = NewModel.objects.all()
    return render(request, "test.html", {"testM": testM, "newM": newM})


def delete_test(request, d):
    testM = TestModel.objects.get(id=d)
    testM.delete()
    # response = redirect('/redirect-success/')
    # return response
    return redirect("/test/")


