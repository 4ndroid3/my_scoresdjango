# Generated by Django 3.1.7 on 2021-03-13 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_delete_users_books'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users_Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_date', models.DateField(blank=True, help_text='Fecha en la que se leyó el libro', null=True, verbose_name='Fecha Leido')),
                ('review', models.TextField(blank=True, help_text='Breve reseña del libro leido.', max_length=500, null=True, verbose_name='Reseña')),
                ('id_book', models.ForeignKey(help_text='Nombre del libro leido', on_delete=django.db.models.deletion.CASCADE, to='books.books', verbose_name='Libro')),
                ('id_profile', models.OneToOneField(help_text='Usuario que leyó el libro', on_delete=django.db.models.deletion.CASCADE, to='users.profile', verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Libro leido',
                'verbose_name_plural': 'Libros leidos',
            },
        ),
    ]
