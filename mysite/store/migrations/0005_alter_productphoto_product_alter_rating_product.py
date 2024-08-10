# Generated by Django 5.0.7 on 2024-07-24 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_descriprion_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productphoto',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='store.product'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='store.product'),
        ),
    ]
