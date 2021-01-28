# Generated by Django 3.1.5 on 2021-01-28 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResizeApp', '0003_auto_20210128_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(blank=True, upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='image',
            name='link',
            field=models.URLField(max_length=255, verbose_name='Ссылка'),
        ),
    ]
