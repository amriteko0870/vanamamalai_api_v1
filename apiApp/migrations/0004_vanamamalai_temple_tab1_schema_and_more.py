# Generated by Django 4.0.3 on 2022-11-28 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0003_gallery_jeeyar_parampara_ponnadikkal_jeeyar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vanamamalai_temple',
            name='tab1_schema',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vanamamalai_temple',
            name='tab2_schema',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vanamamalai_temple',
            name='tab3_schema',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vanamamalai_temple',
            name='tab4_schema',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
