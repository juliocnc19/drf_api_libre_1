from django.db import models
from django.conf import settings

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título de la Noticia")
    content = models.TextField(verbose_name="Contenido de la Noticia")
    published_date = models.DateField(verbose_name="Fecha de Publicación")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="news_author")
    is_featured = models.BooleanField(default=False, verbose_name="¿Destacada?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    def __str__(self):
        return self.title