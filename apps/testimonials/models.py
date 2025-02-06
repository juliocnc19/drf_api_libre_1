from django.db import models
from django.conf import settings

class Testimonial(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="testimonials", on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Contenido del Testimonio")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    is_approved = models.BooleanField(default=False, verbose_name="¿Aprobado?")

    def __str__(self):
        return f"Testimonio de {self.author}"
