# Generated by Django 4.2.4 on 2023-11-07 14:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='urlToImage',
            field=models.ImageField(blank=True, upload_to='news/images/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(blank=True, max_length=250),
        ),
    ]
