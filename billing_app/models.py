from django.db import models
from django.contrib.auth.models import User
from billing_app.signals import create_billing_info
from cart_app.models import Cart, CartAmount
from django.db.models.signals import pre_save
import random
import string
from django.db.models.signals import post_save
from products_app.models import IndividualProduct

class BillingProfileModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bkash_number = models.CharField(max_length=15, null=True)


    def __str__(self):
        return self.user.username


def create_billing_profile(sender, instance, *args, **kwargs):
    BillingProfileModel.objects.create(user=instance)


create_billing_info.connect(create_billing_profile)


class Order(models.Model):
    user = models.ForeignKey(User, default=1)
    order_number = models.CharField(max_length=10)
    order_reference = models.IntegerField(default=-1)
    order_bkash_number = models.CharField(max_length=13, default=0)
    transaction_number = models.CharField(max_length=10, default=0)
    cart = models.ForeignKey(Cart, null=True)
    order_status = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return 'Order number: ' + self.order_number + ' - Order Reference : ' + str(self.id)


def random_number_unique(order):
    qs = Order.objects.filter(order_number=order)
    if qs.count() > 0:
        order = ''.join(random.choice(string.ascii_uppercase +
                                      string.digits) for _ in range(10))
        random_number_unique(order)
    return order


def order_number_generator(sender, instance, *args, **kwargs):
    number = ''.join(random.choice(string.ascii_uppercase +
                                   string.digits) for _ in range(10))
    order = random_number_unique(number)
    instance.order_number = order


pre_save.connect(order_number_generator, sender=Order)


def product_reduction_function(sender, instance, **kwargs):
    if instance.order_status == True:
        qs = CartAmount.objects.filter(cart=instance.cart)
        for product in qs:
            cart_amount = product.amount
            cart_instance = IndividualProduct.objects.get(id=product.products.id)
            in_stock =  cart_instance.in_stock - cart_amount
            cart_instance.in_stock = in_stock
            cart_instance.save()


post_save.connect(product_reduction_function, Order)
