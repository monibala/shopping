# Generated by Django 4.0.5 on 2022-10-29 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0006_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Arunchal Pradesh', 'Arunchal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Delhi', 'Delhi'), ('Goa', 'Goa'), ('Chandigarh', 'Chandigarh'), ('Chattishgarh', 'Chattishgarh'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Madhya Pradesh', 'Madhya Pradesh'), ('punjab', 'punjab'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('West Bengal', 'West Bengal')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Arunchal Pradesh', 'Arunchal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Delhi', 'Delhi'), ('Goa', 'Goa'), ('Chandigarh', 'Chandigarh'), ('Chattishgarh', 'Chattishgarh'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Madhya Pradesh', 'Madhya Pradesh'), ('punjab', 'punjab'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('West Bengal', 'West Bengal')], default='Pending', max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('earing', 'earing'), ('necklace', 'necklace')], max_length=10)),
                ('product_image', models.ImageField(upload_to='productimg')),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product'),
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
