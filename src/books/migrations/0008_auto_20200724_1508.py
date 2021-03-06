# Generated by Django 3.0.7 on 2020-07-24 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0001_initial'),
        ('publisher', '0001_initial'),
        ('books', '0007_auto_20200724_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='publishing',
        ),
        migrations.AddField(
            model_name='books',
            name='publisher',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='publisher', to='publisher.Publisher', verbose_name='Издательство'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='books',
            name='series',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='series', to='series.Series', verbose_name='Серия книг'),
            preserve_default=False,
        ),
    ]
