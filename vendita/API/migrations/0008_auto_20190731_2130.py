# Generated by Django 2.2.3 on 2019-07-31 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0007_book_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='customer_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='sold_out',
            field=models.BooleanField(default=False),
        ),
    ]
