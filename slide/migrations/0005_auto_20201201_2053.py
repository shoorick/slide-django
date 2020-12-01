# Generated by Django 3.1.3 on 2020-12-01 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slide', '0004_auto_20201129_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='slideshow',
            name='stylesheet',
            field=models.TextField(blank=True, verbose_name='CSS rules'),
        ),
        migrations.AlterField(
            model_name='slideshow',
            name='source',
            field=models.TextField(blank=True, verbose_name='Source code'),
        ),
    ]