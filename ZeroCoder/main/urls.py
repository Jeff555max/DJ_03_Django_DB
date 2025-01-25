from django.urls import path
from . import views # точка . говорит о том, что мы находимся и берем из текущей папки main


urlpatterns = [
    path('', views.index, name='home'),  # при переходе на главную страницу мы из views вызываем функцию index
    path('about/', views.about, name='about us'),  # при переходе не на главную страницу, а на страницу например с названием about
                            # мы из views вызываем функцию about

    path('services/', views.services, name='Uslugi'),
    path('contact/', views.contact, name='мои контакты'),



    path('new/', views.new ),
    path('new2/', views.new2 ),
    path('new3/', views.new3 ),
]
