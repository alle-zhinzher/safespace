# Generated by Django 2.2.3 on 2019-07-30 23:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('API', '0006_book_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books_customer', to=settings.AUTH_USER_MODEL),
        ),
    ]