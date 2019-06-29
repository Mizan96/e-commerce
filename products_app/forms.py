from django import forms
from products_app.models import IndividualProduct
from pagedown.widgets import PagedownWidget

class AddProductForm(forms.ModelForm):
    product_description = forms.CharField(widget=PagedownWidget())
    # price = 
    class Meta:
        model = IndividualProduct
        fields = '__all__'

