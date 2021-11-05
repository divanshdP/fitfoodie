# Generated by Django 3.0.6 on 2020-05-12 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cust_name', models.CharField(max_length=50)),
                ('cust_password', models.CharField(max_length=20)),
                ('cust_email', models.EmailField(max_length=50, primary_key=True, serialize=False)),
                ('cust_phone', models.CharField(max_length=10)),
                ('cust_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6)),
                ('cust_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('rest_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('rest_timing', models.CharField(max_length=50)),
                ('rest_logo', models.ImageField(upload_to='rest_logo')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_total', models.CharField(blank=True, max_length=10)),
                ('order_date', models.DateField()),
                ('order_by', models.ManyToManyField(to='app.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='orderItem',
            fields=[
                ('orderitem_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_item_name', models.CharField(max_length=50)),
                ('order_item_price', models.CharField(max_length=50)),
                ('order_item_calories', models.CharField(max_length=50)),
                ('order_item_logo', models.ImageField(default='Null', upload_to='item_logo')),
                ('order_item_quantity', models.IntegerField(default=0)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Orders')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=50)),
                ('item_price', models.CharField(max_length=50)),
                ('item_calories', models.CharField(max_length=50)),
                ('item_quantity', models.IntegerField(default=0)),
                ('item_logo', models.ImageField(default='Null', upload_to='item_logo')),
                ('item_category', models.CharField(choices=[('Burgers', 'Burgers'), ('Drinks', 'Drinks'), ('Sweets', 'Sweets'), ('Pizzas', 'Pizzas')], max_length=50)),
                ('item_rest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Restaurants')),
            ],
        ),
    ]
