from home import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
   path('', views.home, name='home'),
   path('about', views.about, name='about'),
   path('testimonial', views.testimonial, name='testimonial'),
   path('category', views.category, name='category'),
   path('product_detail/<int:pk>', views.product_detail, name='product_detail'),
   path('checkout', views.checkout, name='checkout'),
   path('add-to-cart', views.cart, name='add-to-cart'),
   path('show_cart', views.show_cart, name='show_cart'),
   path('update', views.update, name='update'),
   path('delete', views.delete, name='delete'),
   path('orders', views.orders, name='orders'),
   path('paymentdone', views.paymentdone, name='paymentdone'),
   path('category_detail/<int:pk>', views.category_detail, name='category_detail'),

]
