from django.db import models
from django.contrib.auth.models import User
from accounts_app.signals import create_shipping_profile

# Create your models here.

class ShppingAdressModel(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    country         = models.CharField(max_length=50, null=True)
    contact_name    = models.CharField(max_length=120, null=True)
    apartment       = models.CharField(max_length=255, null=True)
    street          = models.CharField(max_length=255, null=True)
    city            = models.CharField(max_length=120, null=True) 
    zipcode         = models.CharField(max_length=20, null=True)
    telephone       = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user.username


def shpping_address_creating(sender, instance, *args, **kwargs):
    ShppingAdressModel.objects.create(user = instance)


create_shipping_profile.connect(shpping_address_creating)
