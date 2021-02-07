from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from accounts.models import UserProfile
from cars.choices import BRANDS, BODY_STYLES, FUELS, CONDITIONS
from cars.validators import contains_only_digits


class Car(models.Model):
    body_style = models.CharField(choices=BODY_STYLES, blank=False, max_length=20)
    brand = models.CharField(choices=BRANDS, blank=False, max_length=20)
    model = models.CharField(max_length=20, blank=False)
    image = models.ImageField(upload_to='cars', blank=False)
    fuel = models.CharField(choices=FUELS, blank=False, max_length=20)
    price = models.PositiveIntegerField(blank=False)
    year = models.PositiveIntegerField(blank=False, validators=(
        MinValueValidator(1960),
        MaxValueValidator(2022),
        contains_only_digits,
    ))
    horse_power = models.PositiveIntegerField(blank=False)
    condition = models.CharField(choices=CONDITIONS, blank=False, max_length=20)
    description = models.TextField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class Report(models.Model):
    massage = models.TextField()
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    added_by = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
