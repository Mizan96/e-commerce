from django.shortcuts import render
from products_app.models import ProductCategory, IndividualProduct
from rec_engine_app.signals import user_preference_signals 
from rec_engine_app.models import UserPreference
from profile_app.models import ObjectViewed
from cart_app.models import Cart
from wish_app.models import Wish
import random

def not_found_view(request):
    cat = ProductCategory.objects.all()
    context = {
        'cat': cat,
    }
    return render(request, 'base/404.html', context)

def home_view(request):
    wish_obj = []
    if request.user.is_authenticated():
        instance = Wish.objects.filter(user=request.user)
        for x in instance:
            wish_obj.append(x.products)

    cart_obj, new_cart = Cart.objects.new_or_get(request)
    cat = ProductCategory.objects.all()
    featured_products = IndividualProduct.objects.filter(featured=True).order_by('-id')[:9]
    latest_products = IndividualProduct.objects.all().order_by('-timestamp').order_by('-id')[:9]
    best_selling_products = IndividualProduct.objects.filter(best_selling=True).order_by('-id')[:9]
    recommendation = []
    if request.user.is_authenticated() and ObjectViewed.objects.filter(user=request.user).count() > 0:
        user_preference_signals.send(sender=request.user.__class__, request=request)
        prefer_type_id = UserPreference.objects.get(user=request.user).prefer_type
        cat_id = ProductCategory.objects.get(id=prefer_type_id)
        selecting_items = IndividualProduct.objects.filter(product_category=cat_id)
        # random.shuffle(selecting_items)
        # print('France: ',type(selecting_items), selecting_items)
        recommendation = selecting_items[:3]
    context = {
        'cat': cat,
        'featured_products': featured_products,
        'latest_products': latest_products,
        'best_selling_products': best_selling_products,
        'recommendation': recommendation,
        'cart': cart_obj,
        'wish': wish_obj,
    }
    return render(request, 'home/home.html', context)
