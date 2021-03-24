from django.db import models


class Dealer(models.Model):
    """
    Dealer model
    """
    id = models.AutoField(primary_key=True)
    ogrn = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    address = models.CharField(max_length=500)


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
