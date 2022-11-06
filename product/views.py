import re
from django.shortcuts import render
from django.views import View

from home.models import Product,Category,SubCategory


def product(request):
    # precious_stone = Product.objects.all()
    # semi_precious_stone = Product.objects.all()
    # data = {'precious_stone':precious_stone , 'semi_precious_stone':semi_precious_stone}
    # return render(request, 'product.html')
    cat = Category.objects.all()
    subcat = SubCategory.objects.all()
    prod = Product.objects.all()
    res= {'cat':cat, 'subcat':subcat, 'prod':prod}
    return render(request, 'product.html',res)

def antiques(request):
    antiques = Product.objects.filter(category__name='Antiques')
    data = {'antiques':antiques}
    return render(request,'antiques.html',data)      

def bedsheet(request):
    bedsheet = Product.objects.filter(category__name='Bedsheets')
    data = {'bedsheet':bedsheet}
    return render(request,'bedsheet.html',data)   

def cushions(request):
    cushions = Product.objects.filter(category__name='Cushion covers')
    data = {'cushions':cushions}
    return render(request,'cushions.html',data) 

def handbags(request):
    handbags = Product.objects.filter(category__name='Handmade Bags')
    data = {'handbags':handbags}
    return render(request,'handbags.html',data) 

def mandresses(request):
    mandresses = Product.objects.filter(category__name='Man Dresses')
    data = {'mandresses':mandresses}
    return render(request,'mandresses.html',data) 

def sarees(request):
    sarees = Product.objects.filter(category__name='Sarees')
    data = {'sarees':sarees}
    return render(request,'sarees.html',data) 

def salwarsuits(request):
    salwarsuits = Product.objects.filter(category__name='Salwar Suits')
    data = {'salwarsuits':salwarsuits}
    return render(request,'salwarsuits.html',data) 

def scarf(request):
    scarf = Product.objects.filter(category__name='Scarf')
    data = {'scarf':scarf}
    return render(request,'scarf.html',data) 

def stone(request):
    stonedata = Product.objects.filter(category__name='Stone')
    data = {'stonedata':stonedata}
    return render(request,'stone.html',data) 

def wallhangings(request):
    wallhangings = Product.objects.filter(category__name='Wall Hangings')
    data = {'wallhangings':wallhangings}
    return render(request,'wallhangings.html',data) 

def womendresses(request):
    womendresses = Product.objects.filter(category__name='Woomen Dresses')
    data = {'womendresses':womendresses}
    return render(request,'womendresses.html',data)    

def woodenhandicraft(request):
    woodenhandicraft = Product.objects.filter(category__name='Wooden Handicraft')
    data = {'woodenhandicraft':woodenhandicraft}
    return render(request,'woodenhandicraft.html',data)      

def newarrival(request):
    newarrival = Product.objects.filter(category__name='New Arrival')
    data = {'newarrival':newarrival}
    return render(request,'newarrival.html',data)                                    






