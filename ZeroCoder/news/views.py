from django.shortcuts import render
from .models import NewsPost
from .forms import NewsPostForm

# Create your views here.

def news_home(request):
	news = NewsPost.objects.all()
	return render(request, 'news/super_news.html',{'news': news})

def create_news(request):
	form = NewsPostForm()
	return render(request, 'news/add_new_post.html',{'form': form} )



