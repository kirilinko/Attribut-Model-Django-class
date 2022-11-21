from django.db import models
  
class Vehicle(models.Model):
    reg_no = models.IntegerField()
    owner = models.CharField(max_length = 100)
  
class Car(models.Model):
    vehicle = models.OneToOneField(Vehicle, 
          on_delete = models.CASCADE, primary_key = True)
    car_model = models.CharField(max_length = 100)
