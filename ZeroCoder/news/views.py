from django.shortcuts import render
from .models import NewsPost

# Create your views here.

def news_home(request):
	news = NewsPost.objects.all()
	return render(request, 'news/super_news.html',{'news': news})



