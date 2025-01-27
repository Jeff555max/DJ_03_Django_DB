"""
URL configuration for ZeroCoder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('', include('main.urls')), # обработка нашего перехода на главную страницу '' (на файлы приложения main)
    path('news', include('news.urls')), # обработка нашего перехода на файлы приложения news
]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)) # Обслуживание статических файлов во время разработки
# Если вы используете django.contrib.staticfiles, как описано выше, runserver сделает это автоматически,
# когда DEBUG установлен в True. Если у вас нет django.contrib.staticfiles в INSTALLED_APPS, вы все равно можете
# вручную обслуживать статические файлы с помощью представления django.views.static.serve()
# Это не подходит для производственного использования! Некоторые распространенные стратегии развертывания см.
# в разделе Развертывание статических файлов.
# Например, если ваш STATIC_URL определен как static/ вы можете сделать это, добавив следующий фрагмент кода в urls.py:

# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
    # ... the rest of your URLconf goes here ...
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Заметка
# Эта вспомогательная функция работает только в режиме отладки и только в том случае, если данный префикс
# является локальным (например, static/), а не URL (например, http://static.example.com/).
# Кроме того, эта вспомогательная функция обслуживает только фактическую папку STATIC_ROOT;
# Он не выполняет обнаружение статических файлов, как django.contrib.staticfiles.
# Наконец, статические файлы обслуживаются через оболочку на прикладном уровне WSGI. Как следствие,
# запросы статических файлов не проходят через обычную цепочку промежуточного ПО.

