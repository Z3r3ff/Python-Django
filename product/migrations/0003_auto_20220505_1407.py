# Generated by Django 2.2 on 2022-05-05 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
