# Generated by Django 3.0.7 on 2020-07-24 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20200722_1114'),
        ('order', '0002_auto_20200724_0648'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderBy',
            new_name='Order',
        ),
    ]
