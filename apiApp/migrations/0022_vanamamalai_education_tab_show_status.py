# Generated by Django 4.0.3 on 2022-12-31 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0021_vanamamalai_mutt_branches_tab_show_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='vanamamalai_education_tab',
            name='show_status',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
