# Generated by Django 4.2.6 on 2023-10-29 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_relative_url',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
