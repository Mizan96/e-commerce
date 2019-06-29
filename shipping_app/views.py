from django.shortcuts import render, redirect
from shipping_app.forms import ShppingAdressForm
from shipping_app.models import ShppingAdressModel
from products_app.models import ProductCategory
from billing_app.models import Order
from cart_app.models import Cart
from shipping_app.forms import OrderConfirmForm
def shipping_view(request):
    cat = ProductCategory.objects.all()
    if request.user.is_authenticated():
        
        qs = ShppingAdressModel.objects.get(user=request.user)
        form = ShppingAdressForm(request.POST or None, instance=qs) 
        context ={
            'form': form,
            'cat': cat
        }
        if request.method == 'POST' and form.is_valid():
            form.save()
            if request.POST.get('ok') == 'ok':
                return redirect('billing:home')
        return render(request, 'shipping/home.html', context)
            
    else:
        return redirect('accounts:login')

def unconfirm_order(request):
    cat = ProductCategory.objects.all()
    order = Order.objects.filter(order_status=False)
    context = {
        'cat': cat,
        'order': order
    }
    return render(request,'shipping/order_list.html', context)

def unconfirm_detail(requet, pk):
    cat = ProductCategory.objects.all()
    order_instance = Order.objects.get(id=pk)
    cart_instance = order_instance.cart
    items = cart_instance.products.all()
    form = OrderConfirmForm(requet.POST or None, instance=order_instance)
    context = {
        'cat': cat,
        'order_instance': order_instance,
        'items': items,
        'form': form,
        'cart_instance': cart_instance,
    }
    if requet.method == 'POST' and form.is_valid():
        order_form_instance = form.save(commit=False)
        order_form_instance.save()
        return redirect('shipping:order')
    return render(requet, 'shipping/order_detail.html', context)
