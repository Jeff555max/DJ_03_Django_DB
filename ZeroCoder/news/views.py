from django.shortcuts import render
from .models import NewsPost
from .forms import NewsPostForm
from django.shortcuts import redirect


# Create your views here.

def news_home(request):
    news = NewsPost.objects.all()
    return render(request, 'news/super_news.html', {'news': news})


def create_news(request):
    error = ""
    if request.method == 'POST':
        form = NewsPostForm(request.POST)  # Сюда сохранится информация от пользователя.
        if form.is_valid():
            form.save()

        else:
            error = "Данные были заполнены некорректно"
    else:
        form = NewsPostForm()  # Форма создаётся только при GET-запросе

    return render(request, 'news/add_new_post.html', {'form': form, 'error': error})