# Generated by Django 4.0.3 on 2022-11-24 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landing_page',
            name='file_title',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='landing_page',
            name='h1',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='landing_page',
            name='h2',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='landing_page',
            name='layout',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='landing_page',
            name='p',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='landing_page',
            name='yt_title',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]
