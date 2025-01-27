from django.db import models

# Create your models here.
class NewsPost(models.Model):  # NewsPost Имена классов в коде должны соответствуют соглашению о наименовании CapWords
    # (или CamelCase). Это соглашение предполагает, что каждое слово в имени класса начинается с заглавной буквы и
    # не содержит пробелов или символов подчеркивания.
    title = models.CharField('Название новости', max_length=50) # Класс CharField помогает создавать поля, в которых можно записать не более 250 символов.
    short_description = models.CharField('Краткое описание новости', max_length=200)
    text = models.TextField('Какие то новости') # Класс TextField -текст может быть любой длины
    pub_date = models.DateTimeField('Дата публикации') # Дата и время публикации
