# Generated by Django 3.0.7 on 2020-06-18 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Название жанра'),
        ),
    ]
