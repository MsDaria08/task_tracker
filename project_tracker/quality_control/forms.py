from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=100)
    email = forms.EmailField(label='Электронная почта')
    message = forms.CharField(widget=forms.Textarea, label = 'Сообщение')



from django.forms import ModelForm
from .models import BugReport, FeatureRequest

class BugReportForm(ModelForm):
    class Meta:
        model = BugReport
        fields = ['title', 'description', 'status', 'priority', 'project']

class FeatureRequestForm(ModelForm):
    class Meta:
        model = FeatureRequest
        fields = ['title', 'description', 'status', 'priority', 'project']
