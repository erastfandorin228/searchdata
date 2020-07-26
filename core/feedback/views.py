from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .forms import FeedBackForm
from django.shortcuts import render, redirect
from django.views import View
from core.settings import BASE_DIR, SECRET_MAIL, MY_INFO
from django.contrib import messages


class FeedBackView(View):
    def post(self, request):
        next = request.POST.get('next', '/')
        if request.method == 'POST':
            form = FeedBackForm(request.POST)
            if form.is_valid():
                form.save()
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
        # next = next + '#send'
        return redirect(next)
        # return redirect('/#send')
        # return render(request, f'{BASE_DIR}/core/home/templates/index.html', {'form': form})
