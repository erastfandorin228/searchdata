from django import forms


class EmailBaseForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(required=True, widget=forms.Textarea)
