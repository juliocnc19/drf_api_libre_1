from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    mission = models.TextField(verbose_name="Misión", blank=True, null=True)
    vision = models.TextField(verbose_name="Visión", blank=True, null=True)
    history = models.TextField(verbose_name="Historia", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    def __str__(self):
        return self.title