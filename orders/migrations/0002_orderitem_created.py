# Generated by Django 4.2.1 on 2023-07-25 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]