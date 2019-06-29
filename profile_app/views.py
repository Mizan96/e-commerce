from django.shortcuts import render, redirect
from accounts_app.forms import EditProfileForm
from shipping_app.forms import ShppingAdressForm
from billing_app.forms import BillingProfileForm
from profile_app.models import ObjectViewed
from django.core.paginator import Paginator
from search_app.models import SearchHistory
from billing_app.models import Order
from cart_app.models import Cart
from products_app.models import ProductCategory
from django.contrib.auth.models import User
from shipping_app.models import ShppingAdressModel
from billing_app.models import BillingProfileModel

def profile_view(request):
    if not request.user.is_authenticated():
        return redirect('accounts:login')
    cat = ProductCategory.objects.all()
    regi_form = EditProfileForm(request.POST or None, instance=request.user)
    address = ShppingAdressForm(request.POST or None, instance=ShppingAdressModel.objects.get(user=request.user))
    bill = BillingProfileForm(request.POST or None, instance=BillingProfileModel.objects.get(user=request.user))
    if request.method == 'POST':
        if regi_form.is_valid() and 'profile-form' in request.POST:
            regi_form.save()
            return redirect('profile:home')
        if address.is_valid() and 'shipping-form' in request.POST:
            address.save()
            return redirect('profile:home')
        if bill.is_valid() and 'bill-form' in request.POST:
            bill.save()
            return redirect('profile:home')
    context = {
        'regi': regi_form,
        'address': address,
        'bill': bill,
        'cat': cat
    }
    return render(request, 'profile/profile.html', context)

def history_view(request):
    if not request.user.is_authenticated():
        return redirect('accounts:login')
    cat = ProductCategory.objects.all()
    qs = ObjectViewed.objects.filter(user=request.user)
    search = SearchHistory.objects.filter(user=request.user)
    order = Order.objects.filter(user=request.user)
    context = {
        'qs': qs,
        'search': search,
        'order': order,
        'cat': cat
    }
    return render(request, 'profile/history.html', context)

def order_view(request, pk):
    if not request.user.is_authenticated():
        return redirect('accounts:login')
    cat = ProductCategory.objects.all()
    order = Order.objects.get(id=pk)
    qs = Cart.objects.get(id=order.cart_id)
    items = qs.products.all()
    context = {
        'order_reference': order.id,
        'confirm': order.order_status,
        'order_number': order.order_number,
        'sub_total': qs.subtotal,
        'shipping': qs.shipping,
        'total': qs.total,
        'items': items,
        'cat': cat
    }
    return render(request, 'profile/order_details.html', context)
