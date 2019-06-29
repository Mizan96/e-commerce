from django import forms
from billing_app.models import BillingProfileModel
# from django.contrib.admin import widgets


class BillingProfileForm(forms.ModelForm):
    class Meta:
        model = BillingProfileModel
        fields = ['bkash_number']