from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Form
from django.contrib import messages
# Create your views here.

def index(request):
    context = {
        'variable' : 'this is sent'
    }
    return render(request,'index.html',context)
    # return HttpResponse('This is my page')

def about(request):
    return render(request,'about.html')
    # return HttpResponse('This is about page')

def services(request):
    return render(request,'services.html')
    # return HttpResponse('This is service page')

def contact(request):
    return render(request,'contact.html')
    # return HttpResponse('This is contact page')

def james(request):
    return render(request,'james.html')

def lynda(request):
    return render(request,'lynda.html')

def lucas(request):
    return render(request,'lucas.html')

def photo(request):
    return render(request,'p&c.html')

def pic(request):
    return render(request,'f&d.html')

def form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        form = Form(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        form.save()
        messages.success(request, "Your form has been submitted successfully!")
    return render(request,'form.html')