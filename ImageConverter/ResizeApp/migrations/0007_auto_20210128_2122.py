# Generated by Django 3.1.5 on 2021-01-28 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResizeApp', '0006_auto_20210128_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(blank=True, upload_to='', verbose_name='Файл'),
        ),
    ]
