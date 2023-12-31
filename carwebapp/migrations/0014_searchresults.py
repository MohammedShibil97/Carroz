# Generated by Django 3.2.10 on 2023-08-18 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0004_auto_20230813_2332'),
        ('carwebapp', '0013_delete_searchresults'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carapp.carproductdb')),
            ],
        ),
    ]
