from django.urls import render

def index(request):
    return render(request, 'index.html')