from django.db import models
from datetime import datetime
from realtors.models import Realtor

#the way to define a model is through a class
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING) #foreignkey of another table
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True) #parameter "blank = True" makes this field not required
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to = 'photos/%Y/%m/%d/') #anything that we upload from the admin will go to the media folder
    photo_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    lst_date = models.DateTimeField(default=datetime.now, blank=True) #this is imported from the module datetime
    def __str_(self): #this method is to specify which main field we want to display
        return self.title