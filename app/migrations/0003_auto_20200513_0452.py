# Generated by Django 3.0.6 on 2020-05-12 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200513_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_date',
            field=models.DateField(auto_now=True),
        ),
    ]