from django.urls import path
from . import views # точка . говорит о том, что мы находимся и берем из текущей папки main


urlpatterns = [
    path('', views.index),  # при переходе на главную страницу мы из views вызываем функцию index
    path('new', views.new)  # при переходе не на главную страницу, а на страницу например с названием new
                            # мы из views вызываем функцию new
]
