from django.shortcuts import render
# Create your views here.

def home(request):
	return render(request, 'main/new.html') # Создаём метод, который будет запускаться при переходе на страницу news.
                                                         # Мы обратимся к папке templates из приложения main, потому что все папки
                                                         # templates как бы объединяются в одну.


