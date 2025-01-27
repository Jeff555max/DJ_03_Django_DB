from django.db import models

# Create your models here.
class NewsPost(models.Model):
    title = models.CharField('Название новости', max_length=50) # Класс CharField помогает создавать поля, в которых можно записать не более 250 символов.
    short_description = models.CharField('Краткое описание новости', max_length=200)
    text = models.TextField('Какие то новости')
    pub_date = models.DateTimeField('Дата публикации')
