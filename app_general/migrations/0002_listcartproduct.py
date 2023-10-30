# Generated by Django 4.2.6 on 2023-10-30 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0003_product_description_product_sub_title'),
        ('app_general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListCartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_general.client')),
            ],
            options={
                'unique_together': {('user', 'product')},
            },
        ),
    ]
