# Generated by Django 2.2 on 2022-05-06 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20220506_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='Slug'),
        ),
    ]
