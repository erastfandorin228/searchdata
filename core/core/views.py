from django.core.mail import send_mail
from .forms import ContactForm
from django.shortcuts import render
from core.settings import BASE_DIR

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = "{0} New message:\n\n{1}\n\n{2}\n\n{3}".format(name, email, subject,
                                                                           form.cleaned_data['message'],)
            send_mail(subject, message, email, ['ighor.gukov@mail.ru'])
            return render(request, f'{BASE_DIR}/core/home/templates/thank_you.html')
    else:
        form = ContactForm()

    return render(request, f'{BASE_DIR}/core/home/templates/index.html', {'form': form})
