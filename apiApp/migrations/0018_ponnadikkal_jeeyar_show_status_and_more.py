# Generated by Django 4.0.3 on 2022-12-28 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0017_alter_vanamamalai_temple_banner_heading_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ponnadikkal_jeeyar',
            name='show_status',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vanamamalai_education',
            name='show_status',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vanamamalai_mutt_branches',
            name='show_status',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vanamamalai_other_temple',
            name='show_status',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vanamamalai_temple',
            name='show_status',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
