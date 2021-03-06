# Django  Imports
from django.db import models

# Project Imports
from users.models.profile import Profile
from books.models.books import Books

class Users_Books(models.Model):
    """ Guarda los libros leidos y la información de cada usuario

    Se cargan valores obligatorios de:
    - Perfil del usuario que leyo el libro (var: id_profile)
    - Libro leido (var: id_book)

    Valores opcionales:
    - Fecha en que se leyo el libro (var: read_date)
    - Review del libro hecha por el usuario (var: review)
    """

    id_profile = models.OneToOneField(
        Profile, 
        on_delete = models.CASCADE,
        help_text = 'Usuario que leyó el libro',
        verbose_name = 'Nombre',
    )

    id_book = models.ForeignKey(
        Books, 
        on_delete = models.CASCADE,
        help_text = 'Nombre del libro leido',
        verbose_name = 'Libro',
    )

    read_date = models.DateField(
        help_text = 'Fecha en la que se leyó el libro',
        blank = True,
        null=True,
        verbose_name = 'Fecha Leido',
    )

    review = models.TextField(
        max_length = 500,
        help_text = 'Breve reseña del libro leido.',
        blank = True,
        null=True,
        verbose_name = 'Reseña',
    )

    def __str__(self):
        return '{} - {}'.format(self.id_profile, self.id_book)

    class Meta:
        verbose_name = 'Libro leido'
        verbose_name_plural = 'Libros leidos'
    