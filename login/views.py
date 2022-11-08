from django.shortcuts import render
from django.views import View
from django.contrib import messages

from home.models import Customer
from .forms import CustomerRegistrationForm , CustomerProfileForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

# def logged_in(request):
#     return render(request, 'login.html')

class CustomerRegestrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm
        return render(request, 'registration.html',{'form':form})

    def post(self,request):
        form = CustomerRegistrationForm(request.POST)    
        if form.is_valid():
            form.save()
        messages.success(request ,'User Registered Successfully!!')

        return render(request, 'registration.html',{'form':form})

@method_decorator(login_required , name='dispatch')
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm
        return render(request ,'profile.html',{'form':form , 'active':'btn-primary'})  

    def post(self , request):
        form = CustomerProfileForm(request.POST)
        
        if form.is_valid():
            usr =request.user
            name = form.cleaned_data['name']
            mobile = form.cleaned_data['mobile']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']
            res = Customer(user = usr , name = name , mobile=mobile ,locality=locality ,city = city ,zipcode = zipcode ,state =state)
            res.save()  
        messages.success(request ,'Profile Created Successfully!!')
        return render(request ,'profile.html',{'form':form , 'active':'btn-primary'})  
       


def forgot(request):
    return render(request, 'forgot.html')    

def resetpassword(request):
    return render(request,'resetpassword.html')    
@login_required  
def address(request):
    add = Customer.objects.filter(user = request.user)

    return render(request,'address.html',{'add':add ,  'active':'btn-primary'})       
