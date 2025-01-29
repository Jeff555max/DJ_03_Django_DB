from django import forms
from .models import NewsPost

class NewsPostForm(forms.ModelForm):
    class Meta:
        model = NewsPost
        fields = ['title', 'short_description', 'text', 'pub_date',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок новости'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание новости'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Содержание новости', 'rows': 4}),
            'pub_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации', 'type': 'date'}),
            'writers': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Ваше имя'}),
        }
# Добавляем атрибуты к конструкциям, чтобы именно они приняли стили Bootstrap, а не теги.
# Чтобы всё задекорировать, заходим в forms.py. Создаём специальный виджет, в котором будем хранить словарь