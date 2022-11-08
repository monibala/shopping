from django.shortcuts import redirect, render , HttpResponse
from requests import request
from .models import *
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from blog.models import Blog


def home(request):
    
    category = Category.objects.all()
    prod1= Product.objects.all()
    prod2 = Product.objects.filter(category__name='Sarees')
    prod3 = Product.objects.filter(category__name='New Arrival')
    prod4 = Category.objects.filter()
    blg = Blog.objects.all().order_by('date')
    data = {'category': category,'prod1':prod1, 'prod2':prod2, 'blg':blg ,'prod3':prod3 }
   
    return render(request, 'index.html', data)

def blog_category(request):
    
    cats = Product.objects.all()
    
    
   
    data={'cats':cats }
    return render(request,'blog_category.html',data) 


def product_detail(request,pk):
    data = Product.objects.get(pk=pk)
    item_already_in_cart = False
    if request.user.is_authenticated:
        item_already_in_cart = Cart.objects.filter(Q(product=data.id)& Q(user=request.user)).exists()
       

    return render(request,'product_detail.html',{'data':data,'item_already_in_cart':item_already_in_cart})   



def about(request):
    return render(request,'about.html')    

def testimonial(request):
    return render(request,'testimonial.html')     


def category(request):
    return render(request,'category.html')
@login_required
def category_detail(request,pk):
    cat=Category.objects.all()
    # category = Category.objects.get(pk=pk)
    
    subcat = SubCategory.objects.get(pk=pk)
    print(subcat)
    prod = Product.objects.filter(subcategory__name=subcat)
    print(prod)
    context={'cat':cat,'prod':prod}

    return render(request,'product.html',context)   

@login_required
def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount= 0.0
    shipping_amount = 70.0
    total_amount = 0.0 
    cart_product = [ p for p in Cart.objects.all() if p.user == user]
        # print(cart_product)
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.selling_price)
            amount += tempamount
        totalamount = amount + shipping_amount

    return render(request,'checkout.html' , {'add':add , 'totalamount':totalamount , 'cart_items':cart_items}) 

@login_required
def cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    # print(product_id)
    product = Product.objects.get(id = product_id)
    Cart(user=user,product=product).save()

    return redirect('show_cart')

@login_required
def show_cart(request):
    if request.user.is_authenticated:

        user= request.user
        carts = Cart.objects.filter(user=user)

        amount= 0.0
        shipping_amount = 70.0
        total_amount = 0.0 
        cart_product = [ p for p in Cart.objects.all() if p.user == user]
        # print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.selling_price)
                amount += tempamount
                totalamount = amount + shipping_amount


        
            return render(request,'cart.html',{'carts':carts ,'amount':amount ,'totalamount':totalamount })   

        else:
            return render(request,'empty.html')    

          

@login_required
def orders(request):
    op = OrderPlaced.objects.filter(user=request.user)
    return render(request,'orders.html' , {'order_placed':op})    

@login_required
def update(request):
    prod = request.GET.get('min')
    prod1 = request.GET.get('max')
    user = request.user
   
    crt = Cart.objects.filter(user=user , product_id = prod)
    crt1 = Cart.objects.filter(user=user , product_id = prod1)
    print(crt , crt1)
    if prod!=None:
        # print(prod,'//')
        if len(crt)>0:
            ob=crt[0]
            ob.quantity-=1
            ob.save()
           


    elif prod1!=None:
        if len(crt1)>0:
            ob=crt1[0]
            ob.quantity+=1
            ob.save()
           

    else: 
        crts=Cart(user=User.objects.get(id=request.user),product_id=prod,quantity=1)
        crts.save()

    return redirect('show_cart')   

@login_required
def delete(request):
    prod = request.GET.get('remove')
    crt = Cart.objects.filter(user= request.user , product_id = prod)
    crt.delete()

    return redirect('show_cart')  

@login_required
def paymentdone(request):
    user = request.user
    custid = request.GET.get('custid')
    print(custid)
    customer = Customer.objects.get(id = custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer,product=c.product, quantity = c.quantity).save()
        c.delete()

    return redirect('orders')



def search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
   
        if query:
            
            res = Product.objects.filter(title__icontains=query)
            return render(request,'product.html',{'prod':res})
        else:
            print('No information available!!')
            return redirect('home') 
