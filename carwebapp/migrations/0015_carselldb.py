# Generated by Django 3.2.10 on 2023-08-20 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carwebapp', '0014_searchresults'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carselldb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CataName7', models.CharField(blank=True, max_length=100, null=True)),
                ('ProName7', models.CharField(blank=True, max_length=100, null=True)),
                ('Proyear7', models.IntegerField(blank=True, null=True)),
                ('Prokms7', models.IntegerField(blank=True, null=True)),
                ('Profuel7', models.CharField(blank=True, max_length=100, null=True)),
                ('ProPrice7', models.IntegerField(blank=True, null=True)),
                ('ProDescription7', models.CharField(blank=True, max_length=500, null=True)),
                ('ProImage7', models.ImageField(blank=True, null=True, upload_to='product_photo')),
                ('Register', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carwebapp.registerdb')),
            ],
        ),
    ]