# Generated by Django 3.2.10 on 2023-08-09 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0002_auto_20230810_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carproductdb',
            name='Prokms',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
    ]
