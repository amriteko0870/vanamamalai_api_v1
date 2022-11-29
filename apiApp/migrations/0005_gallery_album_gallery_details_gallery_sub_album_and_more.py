# Generated by Django 4.0.3 on 2022-11-29 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0004_vanamamalai_temple_tab1_schema_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='gallery_album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='gallery_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_image', models.TextField()),
                ('banner_heading', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='gallery_sub_album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_album_name', models.TextField()),
                ('sub_album_image', models.TextField()),
                ('sub_album_details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='gallery_youtube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('url', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='gallery',
            name='album_name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery',
            name='details',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery',
            name='name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery',
            name='sub_album_name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
