# Generated by Django 3.1.5 on 2021-02-02 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0011_auto_20210202_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.PositiveIntegerField(),
        ),
    ]
