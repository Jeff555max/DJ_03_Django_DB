from django.shortcuts import render
from django.http import HttpResponse

def new(request):
    return HttpResponse('<h1> Первая страница </h1>')

def new2(request):
    return HttpResponse('<h1> Вторая страница </h1>')

def new3(request):
    return HttpResponse('<h1> Третья страница </h1>')

def index(request):
    return render(request, 'index.html') # файлы HTML пока не созданы

def about(request):
    return render(request, 'about.html') # файлы HTML пока не созданы

def services(request):
    return render(request, 'services.html') # файлы HTML пока не созданы

def contact(request):
    return render(request, 'contact.html') # файлы HTML пока не созданы