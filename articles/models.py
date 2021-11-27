from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scope = models.ManyToManyField('Scope', through='ScopePosition')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class Scope(models.Model):
    scope = models.CharField(max_length=256, verbose_name='Название')
    articles = models.ManyToManyField(Article, related_name='tags')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.scope

class ScopePosition(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='position')
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE, related_name='position')
    is_main = models.BooleanField(verbose_name="Основной тэг")
