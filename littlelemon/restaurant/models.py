from django.db import models

# Create your models here.

class Booking(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField(auto_now=True)
    
class Menu(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()
    
    def __str__(self):
        return self.title+" : "+str(self.price)

