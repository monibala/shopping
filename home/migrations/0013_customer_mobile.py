# Generated by Django 4.0.5 on 2022-11-01 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_product_subcategory_alter_product_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='mobile',
            field=models.IntegerField(null=True),
        ),
    ]
