from django.shortcuts import redirect, render
from .models import Contactus
from django.contrib import messages

# Create your views here.

def contactus(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']
        company_name = request.POST['company_name']
        subject = request.POST['subject']
        message = request.POST['message']
        user_id = request.POST['user_id']
        #TODO: Sanitisation

        contactus = Contactus(full_name=full_name, phone=phone, email=email, company_name=company_name, subject=subject, message=message, user_id=user_id)
        contactus.save()
        messages.success(request, 'Thanks for reaching out!')
        return redirect('contact')


