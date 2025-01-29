from .models import NewsPost
from django.forms import ModelForm, TextInput,Textarea, DateTimeInput


class NewsPostForm(ModelForm):
    class Meta:
        model = NewsPost
        fields = ['title', 'short_description', 'text', 'pub_date',]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок новости'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание новости'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Содержание новости', 'rows': 4}),
            'pub_date':DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации', 'type': 'date'}),
            'writers': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Ваше имя'}),
        }
# Добавляем атрибуты к конструкциям, чтобы именно они приняли стили Bootstrap, а не теги.
# Чтобы всё задекорировать, заходим в forms.py. Создаём специальный виджет, в котором будем хранить словарь