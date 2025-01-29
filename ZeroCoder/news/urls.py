from django.urls import path
from . import views # точка . говорит о том, что мы находимся и берем из текущей папки main


urlpatterns = [
    path('', views.news_home, name='Новости'),  # при переходе на главную страницу adress/news мы из views вызываем функцию news_home
    path('create_news/', views.create_news, name='add_news'), # когда мы заходим на адрес/news/create_news/, запускается функция create_news
    # из файла views, которая открывает страницу add_new_post.html приложения news
    ]
