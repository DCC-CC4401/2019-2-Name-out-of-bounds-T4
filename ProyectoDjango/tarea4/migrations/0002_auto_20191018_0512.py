# Generated by Django 2.2.6 on 2019-10-18 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarea4', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotitos'),
        ),
    ]