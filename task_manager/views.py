from django.http import HttpResponse

def index(request):
    return HttpResponse("Привет! Добро пожаловать в Task Manager.")