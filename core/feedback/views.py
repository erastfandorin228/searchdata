from django.core.mail import send_mail
from .forms import ContactForm
from django.shortcuts import render
from django.views.generic import View
from core.settings import BASE_DIR, SECRET_MAIL




def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = "Name: {0} \nEmail: {1}\nSubject: {2}\nMessage: {3}".format(name, email, subject,
                                                                     form.cleaned_data['message'], )
            send_mail(subject, message, SECRET_MAIL, [SECRET_MAIL])
            return render(request, 'thank_you.html')
    else:
        form = ContactForm()

    return render(request, '/', {'form': form})
