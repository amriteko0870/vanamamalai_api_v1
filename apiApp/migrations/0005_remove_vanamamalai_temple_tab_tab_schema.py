# Generated by Django 4.0.3 on 2022-12-05 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0004_vanamamalai_temple_tab_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vanamamalai_temple_tab',
            name='tab_schema',
        ),
    ]
