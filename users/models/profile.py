# Django Imports
from django.db import models

class Profile(models.Model):
    """Profile Model.

    Informacion informal del usuario, 
    contiene un perfil con imagen, estadisticas y datos adicionales.
    """

    id_users = models.OneToOneField(
        'users.User',
        on_delete = models.CASCADE,
        help_text = 'Nombre del Usuario',
        verbose_name = 'Usuario',
    )
    biography = models.TextField(
        max_length = 500,
        blank=True,
        help_text = 'Breve resumen del Perfil',
        verbose_name = 'Biografía',
    )
    birth_date = models.DateField(
        blank = True,
        null=True,
        verbose_name = 'Fecha de Nacimiento',
        help_text = 'Fecha en la que nació',
    )
    user_img = models.ImageField(
        upload_to = 'profile_img', 
        blank = True,
        null=True,
        help_text = 'Imagen de perfil del usuario',
        verbose_name = 'Imagen de Perfil',
    )
    country = models.ForeignKey(
        'Countries', 
        on_delete = models.CASCADE, 
        verbose_name = 'País',
        blank = True,
        null=True,
        help_text = 'Pais donde vive el usuario',
    )
    # Stats
    books_read = models.PositiveIntegerField(
        default=0, 
        help_text = 'Libros leídos por el usuario',
        verbose_name = 'Libros leídos',
    )
    authors_read = models.PositiveIntegerField(
        default=0,
        help_text = 'Cantidad de autores leídos por el usuario',
        verbose_name = 'Autores leídos'
    )

    def __str__(self):
        return str(self.id_users)
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
    

class Countries(models.Model):
    """Paises del mundo para agregar en el perfil de usuario
    Dicho modelo no tiene vista en el panel de administración
    """
    country_name = models.CharField(
        max_length = 80, 
        verbose_name = 'País',
    )

    def __str__(self):
        return self.country_name
