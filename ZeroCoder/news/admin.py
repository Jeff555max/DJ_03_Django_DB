from django.contrib import admin
from .models import NewsPost # точка не обязательна, она говорит о том что мы берем models из той же
                             # директории где находимся

# Register your models here.

# Регистрируем новую таблицу внутри нашего проекта

admin.site.register(NewsPost)