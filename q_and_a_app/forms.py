from django import forms
from q_and_a_app.models import Question
from pagedown.widgets import PagedownWidget

class QuestionForm(forms.ModelForm):
    question = forms.CharField(widget=PagedownWidget)
    class Meta:
        model = Question
        fields = ['question']