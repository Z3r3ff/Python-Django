# Generated by Django 2.2 on 2022-05-06 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20220506_1011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='slug',
            new_name='product_slug',
        ),
    ]
