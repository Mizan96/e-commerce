from django.db import models
from django.contrib.auth.models import User
from products_app.models import IndividualProduct

# Create your models here.
class Rating(models.Model):
    user        = models.ForeignKey(User)
    product     = models.ForeignKey(IndividualProduct)
    rating      = models.IntegerField(default=0)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)