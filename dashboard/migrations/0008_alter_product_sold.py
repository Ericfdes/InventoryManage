# Generated by Django 4.2.11 on 2024-05-10 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_remove_sale_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sold',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
