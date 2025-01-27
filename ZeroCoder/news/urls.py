from django.urls import path
from . import views # точка . говорит о том, что мы находимся и берем из текущей папки main


urlpatterns = [
    path('', views.news_home, name='Новости'),  # при переходе на главную страницу adress/news мы из views вызываем функцию news_home
    ]
