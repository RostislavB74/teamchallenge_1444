# Generated by Django 5.1.5 on 2025-02-01 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=50, unique=True)),
                ('article', models.CharField(blank=True, max_length=50, null=True)),
                ('type_of_jewelry', models.CharField(max_length=100)),
                ('intended_to', models.CharField(max_length=20)),
                ('product_type', models.CharField(max_length=100)),
                ('subtype', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('design', models.TextField()),
                ('metal', models.CharField(max_length=50)),
                ('carat', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('metal_color', models.CharField(max_length=50)),
                ('material_color', models.CharField(max_length=50)),
                ('stone', models.CharField(blank=True, max_length=50, null=True)),
                ('stone_color', models.CharField(blank=True, max_length=50, null=True)),
                ('inlay', models.CharField(blank=True, max_length=50, null=True)),
                ('inlay_characteristics', models.TextField(blank=True, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('dimensions', models.CharField(blank=True, max_length=100, null=True)),
                ('size', models.CharField(blank=True, max_length=20, null=True)),
                ('gift_reason', models.CharField(blank=True, max_length=100, null=True)),
                ('clasp_type', models.CharField(blank=True, max_length=50, null=True)),
                ('style', models.CharField(max_length=50)),
                ('weave_type', models.CharField(blank=True, max_length=50, null=True)),
                ('material', models.CharField(blank=True, max_length=100, null=True)),
                ('coating', models.CharField(blank=True, max_length=50, null=True)),
                ('gold_plating', models.CharField(blank=True, max_length=50, null=True)),
                ('collection', models.CharField(max_length=50)),
                ('set', models.BooleanField(default=False)),
                ('country_of_origin', models.CharField(max_length=50)),
                ('brand_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
