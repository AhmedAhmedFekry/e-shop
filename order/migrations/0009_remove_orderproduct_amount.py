# Generated by Django 3.1.6 on 2021-03-17 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_remove_order_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='amount',
        ),
    ]