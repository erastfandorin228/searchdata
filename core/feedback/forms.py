from django import forms

from .models import Feedback


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'subject', 'message')

# без моделей это делается так
# class ContactForm(forms.Form):
#    name = forms.CharField(max_length=25)
#    email = forms.EmailField()
#    subject = forms.CharField(max_length=100)
#    message = forms.CharField(required=True, widget=forms.Textarea)
