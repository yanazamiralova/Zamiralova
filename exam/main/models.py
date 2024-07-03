from django.db import models

class Statement(models.Model):
    numbers = models.CharField(max_length=9)
    description = models.TextField()
    stat = models.ForeignKey('Stat', verbose_name='Статус', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['numbers']
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Stat(models.Model):
    title = models.CharField(verbose_name='Название', max_length=60)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'