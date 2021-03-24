from django.db import models
from django.core.exceptions import ValidationError


class Dealer(models.Model):
    """
    Dealer model
    """
    id = models.AutoField(primary_key=True)
    ogrn = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    address = models.CharField(max_length=500)

    def clean(self):
        if not str(self.ogrn).isdigit():
            raise ValidationError(
                'ogrn must be integer'
            )


class Auto(models.Model):
    """
    Car model
    top_speed in km/h
    weight in kg
    mileage in km
    """
    id = models.AutoField(primary_key=True)
    car_brand = models.CharField(max_length=300)
    model_name = models.CharField(max_length=300)
    vin = models.CharField(unique=True, max_length=17)
    top_speed = models.IntegerField()
    weight = models.IntegerField()
    mileage = models.IntegerField()
    horsepower = models.IntegerField()
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)

    def clean(self):
        if not str(self.top_speed).isdigit():
            raise ValidationError(
                'top_speed must be integer'
            )
        elif not str(self.weight).isdigit():
            raise ValidationError(
                'weight must be integer'
            )
        elif not str(self.mileage).isdigit():
            raise ValidationError(
                'mileage must be integer'
            )
        elif not str(self.horsepower).isdigit():
            raise ValidationError(
                'horsepower must be integer'
            )
