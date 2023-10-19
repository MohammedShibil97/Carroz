# Generated by Django 3.2.10 on 2023-08-20 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0004_auto_20230813_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='ratingdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Yr_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Email8', models.EmailField(blank=True, max_length=100, null=True)),
                ('Yr_rating', models.CharField(blank=True, max_length=500, null=True)),
                ('Yr_photo', models.ImageField(blank=True, null=True, upload_to='Client_photo')),
            ],
        ),
    ]
