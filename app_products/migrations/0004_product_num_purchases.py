# Generated by Django 4.2.6 on 2023-10-30 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0003_product_description_product_sub_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='num_purchases',
            field=models.IntegerField(default=0),
        ),
    ]
