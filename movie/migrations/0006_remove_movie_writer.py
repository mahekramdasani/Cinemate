# Generated by Django 4.2.4 on 2023-11-07 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_remove_movie_awards'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='Writer',
        ),
    ]