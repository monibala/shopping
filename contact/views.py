from django.shortcuts import render
from contact.models import contacts
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = contacts(name=name,email=email,subject=subject,message=message)
        data.save()
        messages.success(request,'Message Sent Successfully!!')
    return render(request , 'contact.html')
