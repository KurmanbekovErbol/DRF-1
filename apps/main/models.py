from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Загаловок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    image = models.ImageField(
        upload_to='photo/',
        verbose_name='Фото'
    )
    video = models.FileField(
        upload_to="video/",
        verbose_name="Видео"
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'