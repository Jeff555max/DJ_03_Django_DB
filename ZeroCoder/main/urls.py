from django.urls import path
from . import views # точка . говорит о том, что мы находимся и берем из текущей папки main


urlpatterns = [
    path('', views.index, name='index'),  # при переходе на главную страницу мы из views вызываем функцию index
    path('about/', views.about, name='about'),  # при переходе не на главную страницу, а на страницу например с названием about
                            # мы из views вызываем функцию about
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('new/', views.new ),
    path('new2/', views.new2 ),
    path('new3/', views.new3 ),
]
