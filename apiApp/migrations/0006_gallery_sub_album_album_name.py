# Generated by Django 4.0.3 on 2022-11-29 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0005_gallery_album_gallery_details_gallery_sub_album_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery_sub_album',
            name='album_name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
