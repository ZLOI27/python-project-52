from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")

'''def test_error(request):
    a = None
    a.hello()  # This will raise AttributeError
    return HttpResponse("This will not be reached")'''



def test_error(request):
    raise Exception("Rollbar test")