# Generated by Django 3.1.5 on 2021-02-02 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_auto_20210130_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='where',
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(choices=[('', ''), ('Audi', 'Audi'), ('BMW', 'BMW'), ('Chevrolet', 'Chevrolet'), ('Ford', 'Ford'), ('Toyota', 'Toyota'), ('Honda', 'Honda'), ('Mercedes', 'Mercedes'), ('Volkswagen', 'Volkswagen'), ('Mazda', 'Mazda'), ('Tesla', 'Tesla')], max_length=20),
        ),
    ]
