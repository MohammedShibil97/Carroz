# Generated by Django 3.2.10 on 2023-08-09 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carproductdb',
            name='Profuel',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='carproductdb',
            name='Prokms',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
    ]