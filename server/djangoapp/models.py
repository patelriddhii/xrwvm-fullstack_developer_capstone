

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Add any other fields you would like
    country_of_origin = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    # Many-to-One relationship to CarMake
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    # Dealer ID refers to a dealer in Cloudant database
    dealer_id = models.IntegerField()
    
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('TRUCK', 'Truck')
    ]
    type = models.CharField(
        max_length=10,
        choices=CAR_TYPES,
        default='SUV'
    )
    
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ]
    )

    def __str__(self):
        return f"{self.car_make.name} {self.name}"
