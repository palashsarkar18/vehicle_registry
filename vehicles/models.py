from django.db import models


class Vehicle(models.Model):
    model_year = models.CharField(max_length=4)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    rejection_percentage = models.CharField(max_length=10)
    reason_1 = models.CharField(max_length=100)
    reason_2 = models.CharField(max_length=100)
    reason_3 = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.make} {self.model} ({self.model_year})"
