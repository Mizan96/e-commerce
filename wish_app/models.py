from django.db import models
from django.contrib.auth.models import User
from products_app.models import IndividualProduct


class Wish(models.Model):
    user        = models.ForeignKey(User)
    products    = models.ForeignKey(IndividualProduct)
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)