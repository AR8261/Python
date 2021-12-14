from django.db import models

# Create your models here.
class Building(models.Model):
    number=models.IntegerField()
    street=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.number} {self.street}"


class Apartment(models.Model):
    number=models.IntegerField()
    monthly_rent=models.IntegerField()
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.building.number} {self.building.street} apt {self.number}"




class Tenant(models.Model):
    apartment=models.ForeignKey(Apartment,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)  # first_name varchar(30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    MALE="M"
    FEMALE="F"
    OTHER="O"
    Gender_type=[(MALE,"Male"),(FEMALE,"Female"),(OTHER,"Other")]
    gender = models.CharField(max_length=1,choices=Gender_type,default='O')


    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} , {self.gender}"

class Director(models.Model):
    name = models.CharField(max_length=64)

class Movie(models.Model):
    title = models.CharField(max_length=255, primary_key=True)
    lead = models.CharField(max_length=255)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)