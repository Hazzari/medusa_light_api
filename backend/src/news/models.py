
import datetime

from django.db import models


class NewsPost(models.Model):
    date = models.DateField('Дата публикации', default=datetime.date.today)
    # unique - избавляемся от дублей
    subject = models.CharField('Заголовок публикации', max_length=256, unique=True)
    content = models.TextField('Текст новости')

    def __str__(self):
        return f'{self.subject}'

    class Meta:
        get_latest_by = ['-data']
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
