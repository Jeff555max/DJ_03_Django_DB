from django.shortcuts import render
# from django.http import HttpResponse # можно уже удалить, это для создания простых страниц с текстом


def index(request):
    data = {
        'caption': "WolfDjango"
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def contact(request):
    return render(request, 'main/contact.html')






# def new2(request):
    return HttpResponse('<h1> Вторая страница </h1>') # можно уже удалить, это для создания простых страниц с текстом

# def new3(request):
    return HttpResponse('<h1> Третья страница </h1>')# можно уже удалить, это для создания простых страниц с текстом