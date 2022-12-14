# Generated by Django 4.0.3 on 2022-12-05 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0005_remove_vanamamalai_temple_tab_tab_schema'),
    ]

    operations = [
        migrations.CreateModel(
            name='vanamamalai_other_temple_tab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temple_id', models.IntegerField()),
                ('tab_heading', models.TextField()),
                ('tab_desc', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='vanamamalai_other_temple',
            name='banner_heading',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vanamamalai_other_temple',
            name='banner_image',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vanamamalai_other_temple',
            name='content_image',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vanamamalai_other_temple',
            name='content_subtitle',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vanamamalai_other_temple',
            name='content_title',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
