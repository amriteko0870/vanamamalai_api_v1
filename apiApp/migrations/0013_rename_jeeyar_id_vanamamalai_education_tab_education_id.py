# Generated by Django 4.0.3 on 2022-12-06 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0012_vanamamalai_education_tab_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vanamamalai_education_tab',
            old_name='jeeyar_id',
            new_name='education_id',
        ),
    ]