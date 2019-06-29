from django import forms
from review_app.models import ReviewModel 
from pagedown.widgets import PagedownWidget

class ReviewForm(forms.ModelForm):
    review = forms.CharField(widget=PagedownWidget)
    class Meta:
        model = ReviewModel
        fields = ['review']