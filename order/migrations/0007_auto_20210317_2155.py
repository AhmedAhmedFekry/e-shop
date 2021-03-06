# Generated by Django 3.1.6 on 2021-03-17 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_auto_20210225_1753'),
        ('order', '0006_orderproduct_variant'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-create_at',)},
        ),
        migrations.RemoveField(
            model_name='order',
            name='code',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='create_at',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='status',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='update_at',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='user',
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.order'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='product.product'),
        ),
    ]
