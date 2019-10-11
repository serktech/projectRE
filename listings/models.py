from django.db import models
from datetime import datetime
from realtors.models import Realtor


class Listing(models.Model):
    # listing_id = models.
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200, default=None)
    address = models.CharField(max_length=200, default=None)
    city = models.CharField(max_length=200, default=None)
    state = models.CharField(max_length=200, default=None)
    zipcode = models.CharField(max_length=20, default=None)
    description = models.TextField(blank=True)
    bedrooms = models.IntegerField(default=None)
    guests = models.IntegerField(default=None)
    lastminute = models.CharField(max_length=20, default=None)
    gender = models.CharField(max_length=20, default=None)
    kidfriendly = models.CharField(max_length=20, default=None)
    smokingallow = models.CharField(max_length=20, default=None)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
