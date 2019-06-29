from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
import random
import os

# Create your models here.

def get_file_name(filename):
    name, extension = os.path.splitext(filename)
    file_new_name = random.randint(1111111111,9999999999)
    return str(file_new_name) + extension

def get_dir(instance, filename):
    return 'products/'+ instance.slug+'/'+ get_file_name(filename)

class ProductCategory(models.Model):
    title           = models.CharField(max_length=255)
    image           = models.ImageField(upload_to="product_category", blank=True, null=True)
    updated         = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class IndividualProduct(models.Model):
    product_category    = models.ForeignKey(ProductCategory)
    title               = models.CharField(max_length = 100)
    slug                = models.CharField(max_length = 120, null=True, blank=True)
    in_stock            = models.IntegerField(default=20)
    price               = models.IntegerField(default=0)
    image1              = models.ImageField(upload_to=get_dir, blank=True, null=True)
    image2              = models.ImageField(upload_to=get_dir, blank=True, null=True)
    image3              = models.ImageField(upload_to=get_dir, blank=True, null=True)
    image4              = models.ImageField(upload_to=get_dir, blank=True, null=True)
    image5              = models.ImageField(upload_to=get_dir, blank=True, null=True)
    featured            = models.BooleanField(default=False)
    best_selling        = models.BooleanField(default=False)
    product_description = models.TextField()
    updated             = models.DateTimeField(auto_now=True)
    timestamp           = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


def create_slug(title):
    print(title)
    qs = IndividualProduct.objects.filter(slug=title)
    if qs.exists():
        title = title + str(qs.last().id) 
        create_slug(title)
    else:
        return title # this is causing infinite recursion
    return title

def slug_generator_for_image_folder(sender, instance, *args, **kwargs):
    if instance.slug == None:
        title = slugify(instance.title)
        instance.slug = create_slug(title)
        instance.save()
    else:
        pass
        


pre_save.connect(slug_generator_for_image_folder, sender=IndividualProduct)
