# Generated by Django 4.0.3 on 2023-01-02 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0025_alter_jeeyars_banner_heading_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jeeyars',
            name='jeeyar_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
