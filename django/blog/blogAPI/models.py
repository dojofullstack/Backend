from django.db import models

# Create your models here.


class ArticuloBlog(models.Model):
    # si la columna es opcional agregar  blank=True
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='imagenes-blog')
    slug_article = models.SlugField(max_length=90)
    date_created = models.DateField(auto_now=True)
    description = models.TextField()
