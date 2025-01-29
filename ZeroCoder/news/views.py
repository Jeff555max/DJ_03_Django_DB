from django.shortcuts import render, redirect
from .models import NewsPost
from .forms import NewsPostForm


def news_home(request):
    news = NewsPost.objects.all()
    return render(request, 'news/super_news.html', {'news': news})


def create_news(request):
    error = ""
    if request.method == 'POST':
        form = NewsPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')  # Убедитесь, что в urls.py есть path с name='news_home'
        else:
            error = "Данные были заполнены некорректно"
    else:
        form = NewsPostForm()  # Форма создаётся при GET-запросе

    return render(request, 'news/add_new_post.html', {'form': form, 'error': error})
