from django.db import models


# Create your models here.
class Feedback(models.Model):
    # форма обратной связи
    name = models.CharField('Имя', max_length=25)
    email = models.EmailField('Email')
    subject = models.CharField('Тема', max_length=100)
    message = models.TextField('Сообщение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Форма обратной связи"
