from django import forms
from shipping_app.models import ShppingAdressModel
from billing_app.models import Order

class ShppingAdressForm(forms.ModelForm):
    class Meta:
        model = ShppingAdressModel
        fields = ['country', 'contact_name','apartment', 'street', 'city', 'zipcode', 'telephone']

class OrderConfirmForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_status']