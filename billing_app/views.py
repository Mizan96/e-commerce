from django.shortcuts import render, redirect
from billing_app.models import Order
from cart_app.models import Cart, CartAmount
from billing_app.forms import BillingProfileForm
from billing_app.models import BillingProfileModel
from products_app.models import ProductCategory, IndividualProduct
from billing_app import gmail
from django.http import  HttpResponseNotFound


def billing_view(request):
    cat = ProductCategory.objects.all()
    cart_obj = Cart.objects.get(id=request.session['cart_id'])
    qs  = Order.objects.filter(cart=cart_obj)
    if qs.count() > 0:
        instance = qs.first()
    else:
        instance = Order.objects.create(cart=cart_obj, user=request.user)
    if request.user.is_authenticated():
        profile = BillingProfileModel.objects.get(user=request.user)
        form = BillingProfileForm(request.POST or None, instance=profile)
    context={
        'reference': instance.id,
        'order_number': instance.order_number,
        'sub_total': cart_obj.subtotal,
        'shipping': cart_obj.shipping,
        'total': cart_obj.total,
        'form': form,
        'cat': cat
    }
    if request.method == 'POST' and form.is_valid():
        request.session['order_reference']  = instance.id
        request.session['order_payment']    = float(cart_obj.total)
        request.session['bkash_number']     = form.cleaned_data.get('bkash_number')
        order_instance = Order.objects.get(id=instance.id)
        order_instance.order_bkash_number = form.cleaned_data.get('bkash_number')
        order_instance.transaction_number = request.POST.get('transaction_number')
        order_instance.save()
        form.save()
        if request.POST.get('ok') == 'ok':
            request.session['gmail_data']  = gmail.get_payment_info()
            return redirect('billing:confirm')
    return render(request, 'billing/home.html', context)
        



def confirm_view(request):
    # print(request.session['in_cart'] )
    try:
        cart_id = request.session['in_cart']
    except:
        return redirect('404-page')
    # if request.session['in_cart'] == None:
    #     return HttpResponseNotFound('<h1>Page not found</h1>')
    order_confirm = False
    for x in request.session['gmail_data']:
        print(int(x['reference']), int(x['number']), float(x['amount']))
        if int(request.session['order_reference']) == int(x['reference']):
            if int(x['number']) == int(request.session['bkash_number']) and float(x['amount']) == float(request.session['order_payment']):
                order_confirm = True
                order_obj = Order.objects.get(cart=request.session['cart_id'])
                order_obj.order_status = True
                order_obj.save()
            # print('From gmail:',x['number'], x['amount']) 
    # print(request.session['gmail_data'])
    print(request.session['order_reference'])
    print(request.session['order_payment'])
    print(request.session['bkash_number'])       
    del request.session['in_cart']
    del request.session['cart_id']
    cat = ProductCategory.objects.all()
    context = {
        'cat': cat,
        'order_confirm': order_confirm
    }
    return render(request, 'billing/successful.html', context)
