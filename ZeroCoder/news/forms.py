from .models import NewsPost
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
# Форму нужно связать с моделью, с базой данных
class NewsPostForm(ModelForm):
	class Meta:
		model = NewsPost
		fields = ['title', 'short_description', 'text', 'pub_date'] # поля берутся из файла news.models
        widgets = {
    'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок новости'}),
    'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание новости'}),
    'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Содержание новости'}),
    'pub_date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'})
}
# Добавляем атрибуты к конструкциям, чтобы именно они приняли стили Bootstrap, а не теги.
# Чтобы всё задекорировать, заходим в forms.py. Создаём специальный виджет, в котором будем хранить словарь.