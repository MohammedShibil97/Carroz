# Generated by Django 3.2.10 on 2023-08-10 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carwebapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Yname', models.CharField(blank=True, max_length=100, null=True)),
                ('Yemail', models.EmailField(blank=True, max_length=100, null=True)),
                ('Subjct', models.CharField(blank=True, max_length=100, null=True)),
                ('Messeges', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
