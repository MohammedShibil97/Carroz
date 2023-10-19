# Generated by Django 3.2.10 on 2023-08-20 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carwebapp', '0015_carselldb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carselldb',
            name='Register',
        ),
        migrations.AddField(
            model_name='carselldb',
            name='Contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carwebapp.contactdb'),
        ),
        migrations.AddField(
            model_name='carselldb',
            name='Yrmob',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]