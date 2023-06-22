from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
import os
from django.conf import settings
from portfolio.models import Contact
from django.core.mail import send_mail
from django.core.mail.message import EmailMessage
from django.conf import settings
from django.core import mail

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')

def resume(request):
    return render(request, 'resume.html')



def contact(request):
    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fphoneno=request.POST.get('num')
        fdesc=request.POST.get('desc')
        query=Contact(name=fname,email=femail,phonenumber=fphoneno,description=fdesc)
        query.save()
        messages.success(request,"Thanks for contacting us. We will get by you Soon!")

        return redirect('/contact')

    return render(request,'contact.html')
