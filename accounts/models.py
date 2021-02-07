from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MinLengthValidator, MaxLengthValidator
from django.db import models

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField

from accounts.choices import REGIONS
from accounts.validators import contains_only_digits


class UserProfile(models.Model):
    phone_number = models.CharField(max_length=10,blank=False,unique=True,validators=(
        MinLengthValidator(10),
        contains_only_digits,
    ))
    region = models.CharField(choices=REGIONS,max_length=20,blank=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

