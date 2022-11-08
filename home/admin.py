from django.contrib import admin

from .models import *

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','zipcode','state']

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id','image','name']  

@admin.register(SubCategory)
class SubCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id','name']      



@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','category','title','selling_price','discounted_price','description','product_image']    



@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']    


@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product','quantity','ordered_date','status']      
