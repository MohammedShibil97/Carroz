# Generated by Django 3.2.10 on 2023-08-14 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carwebapp', '0006_remove_checkoutdb_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutdb',
            name='Register',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carwebapp.registerdb'),
        ),
    ]