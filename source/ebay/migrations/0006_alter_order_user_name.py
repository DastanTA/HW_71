# Generated by Django 4.1.4 on 2023-01-10 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebay', '0005_rename_orderinbasket_orderproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user_name',
            field=models.CharField(max_length=50, verbose_name='имя'),
        ),
    ]
