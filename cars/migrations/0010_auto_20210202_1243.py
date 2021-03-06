# Generated by Django 3.1.5 on 2021-02-02 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_auto_20210202_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='transmission',
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(choices=[('Audi', 'Audi'), ('BMW', 'BMW'), ('Chevrolet', 'Chevrolet'), ('Ford', 'Ford'), ('Toyota', 'Toyota'), ('Honda', 'Honda'), ('Mercedes', 'Mercedes'), ('Volkswagen', 'Volkswagen'), ('Mazda', 'Mazda'), ('Tesla', 'Tesla')], max_length=20),
        ),
        migrations.AlterField(
            model_name='car',
            name='condition',
            field=models.CharField(choices=[('New', 'New'), ('Used', 'Used'), ('For parts', 'For parts')], max_length=20),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel',
            field=models.CharField(choices=[('Gasoline', 'Gasoline'), ('Diesel', 'Diesel'), ('Gas', 'Gas'), ('Еlectric', 'Еlectric')], max_length=20),
        ),
    ]
