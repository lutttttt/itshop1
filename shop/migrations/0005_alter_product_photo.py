# Generated by Django 5.1.4 on 2025-03-10 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_photo_alter_seller_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(default='a', upload_to=''),
        ),
    ]
