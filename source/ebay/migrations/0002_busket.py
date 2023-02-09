# Generated by Django 4.1.4 on 2022-12-13 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ebay', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Busket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='basket', to='ebay.product', verbose_name='продукт')),
            ],
        ),
    ]
