from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.http import HttpResponseRedirect

from django.core.mail import send_mail

def index(request):
    form = ContactForm()
    return render(request, 'resume/index.html', {'form':form})

def ContactMe(request):
    form = ContactForm()
    # if form.is_valid():
    # request.POST.get('username')
    sender = request.POST.get('email')
    subject = 'My Portfolio : '+request.POST.get('name')
    message = request.POST.get('message')

    recipients = ['yadavamit.ay@gmail.com']
    send_mail(subject, message, sender, recipients)
    return HttpResponseRedirect('/')
    # return render(request, 'resume/index.html', {'form':form})


# Create your views here.
