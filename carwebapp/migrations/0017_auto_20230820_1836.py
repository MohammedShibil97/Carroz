# Generated by Django 3.2.10 on 2023-08-20 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carwebapp', '0016_auto_20230820_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carselldb',
            name='Contact',
        ),
        migrations.AddField(
            model_name='carselldb',
            name='Yemail2',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='carselldb',
            name='Yname2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
