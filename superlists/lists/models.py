from django.db import models
from django.urls import reverse


# Create your models here.
class List(models.Model):
    """Список"""

    def get_absolute_url(self):
        """Получить абсолютный url"""
        return reverse('view_list', args=[self.id])


class Item(models.Model):
    """Элемент списка"""
    text = models.TextField(default="")
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)

    def __str__(self):
        """Строковое представление"""
        return self.text

    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text')
