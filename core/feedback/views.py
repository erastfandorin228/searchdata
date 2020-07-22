from django.core.mail import send_mail
from django.http import HttpResponseRedirect

from .forms import ContactForm
from django.shortcuts import render, redirect
from django.views.generic import View
from core.settings import BASE_DIR, SECRET_MAIL, MY_INFO
from django.contrib import messages


def contact_us(request):
    global next
    if request.method == 'POST':
        form = ContactForm(request.POST)
        next = request.POST.get('next', '/')

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = "Name: {0} \nEmail: {1}\nSubject: {2}\nMessage: {3}".format(name, email, subject,
                                                                                  form.cleaned_data['message'], )
            send_mail(subject, message, SECRET_MAIL, [SECRET_MAIL])
            messages.add_message(request, MY_INFO, 'Ваше сообщение успешно отправлено! Мы Вам обязательно ответим!')



            # return render(request, 'thank_you.html')
        else:
            messages.add_message(request, MY_INFO, 'Введены неверные данные! Ваше сообщение не отправлено!')
        # form = ContactForm()
    #next = next + '#send'
    return HttpResponseRedirect(next)
    # return redirect('/#send')
    # return render(request, f'{BASE_DIR}/core/home/templates/index.html', {'form': form})
