from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(required=True, widget=forms.Textarea)
