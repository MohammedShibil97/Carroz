# Generated by Django 3.2.10 on 2023-08-13 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carwebapp', '0005_auto_20230813_2332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkoutdb',
            name='Register',
        ),
    ]
