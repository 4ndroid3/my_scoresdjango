# Django Imports
from django.db import models

class Books(models.Model):
    """Contiene los libros que van ingresando los usuarios
    
    Se cargan valores obligatorios de:
    - Titulo
    - Autor
    
    Valores opcionales:
    - Año publicación
    - Cantidad de páginas
    - Imagen de la portada del libro
    """

    title = models.CharField(
        max_length = 80,
        help_text = 'Título del libro',
        verbose_name = 'Título',
    )

    author = models.CharField(
        max_length = 80,
        help_text = 'Autor del libro.',
        verbose_name = 'Autor',
    )

    year = models.PositiveIntegerField(
        help_text = 'Año en que se publico el libro.',
        blank = True,
        null=True,
        verbose_name = 'Año de publicación',
    )

    pages = models.PositiveIntegerField(
        help_text = 'Cantidad de hojas que tiene el libro.',
        blank = True,
        null=True,
        verbose_name = 'Cantidad de Hojas',
    )

    img_cover = models.ImageField(
        upload_to = 'books', 
        blank = True,
        null=True,
        help_text = 'Imagen de la portada',
        verbose_name = 'Portada',
    )

    def __str__(self):
        return '{} - {}'.format(self.author, self.title)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'