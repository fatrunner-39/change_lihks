from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class ChangeURL(models.Model):
    fullurl = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.fullurl

    class Meta:
        verbose_name = 'Модель сокращения ссылок'
        verbose_name_plural = 'Модели сокращения ссылок'

    def get_absolute_url(self):
        return reverse('links')
