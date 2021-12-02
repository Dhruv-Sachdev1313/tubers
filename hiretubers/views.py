from django.shortcuts import redirect, render
from .models import Hiretuber
from django.contrib import messages

# Create your views here.
def hiretuber(request):
    print('method called')
    if request.method == 'POST':
        print('request recieved!')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']
        email = request.POST['email']
        city = request.POST['city']
        phone = request.POST['phone']
        state = request.POST['state']
        user_id = request.POST['user_id']
        message = request.POST['message']

        # TODO: do all sanitisation
        hiretuber = Hiretuber(first_name=first_name, last_name=last_name, tuber_id=tuber_id, tuber_name= tuber_name, email=email,city=city, phone=phone, state=state, user_id=user_id, message= message)
        print('instance created')
        hiretuber.save()
        print('instance saved')
        messages.success(request, 'Thanks for reaching out!')
        print('success')
        return redirect('youtubers')