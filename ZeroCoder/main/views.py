from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def contact(request):
    return render(request, 'main/contact.html')



def new(request):
    return HttpResponse('<h1> Первая страница </h1>')

def new2(request):
    return HttpResponse('<h1> Вторая страница </h1>')

def new3(request):
    return HttpResponse('<h1> Третья страница </h1>')