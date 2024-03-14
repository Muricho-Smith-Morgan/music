from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages 
from .models import *

# Create your views here.
def index_page(request):
    return render(request, 'music/index.html')

def about_page(request):
    return render(request, 'music/About.html')

def get_details(request):
    if request.method == 'POST':
        name = request.POST['firstname']
        phone_no = request.POST['phonenumber']
        mail = request.POST['email']
        mode = request.POST['Classes']
        instrument = request.POST['learning']

        save_details = BookSession.objects.create(username=name, phone_no=phone_no, user_email=mail, learning_mode=mode, instrument=instrument)
        save_details.save()

        messages.success(request, 'Session booked succesfully!')
        return redirect('book')
    
    return render(request, 'music/book.html')