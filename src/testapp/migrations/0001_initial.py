# Generated by Django 3.0.6 on 2020-06-04 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parsing_browser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('browser', models.CharField(blank=True, max_length=10, null=True, verbose_name='Browser')),
            ],
        ),
        migrations.CreateModel(
            name='Parsing_date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Parsing_ip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP')),
            ],
        ),
        migrations.CreateModel(
            name='Parsing_string',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('string', models.TextField(blank=True, null=True, verbose_name='String')),
            ],
        ),
    ]
