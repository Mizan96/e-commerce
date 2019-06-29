from django.shortcuts import render, redirect
from wish_app.models import Wish
from products_app.models import IndividualProduct
from django.http import JsonResponse

def wish_update_view(request):
    product_id = request.POST.get('wish_product_id')
    instance   = IndividualProduct.objects.get(id=product_id)
    qs = Wish.objects.filter(user=request.user, products=instance)
    if qs.count() > 0:
        qs.first().delete()
        added = False
    else:
        Wish.objects.create(user=request.user, products=instance)
        added = True
    if request.is_ajax(): 
        # print("Ajax request")
        json_data = {
            "added": added,
            "removed": not added,
        }
        return JsonResponse(json_data)
    return redirect('/')
