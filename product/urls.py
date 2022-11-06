from product import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
  
   path('product', views.product, name='product'),
   path('newarrival', views.newarrival, name='newarrival'),

   path('antiques', views.antiques, name='antiques'),
   path('bedsheet', views.bedsheet, name='bedsheet'),
   path('cushions', views.cushions, name='cushions'),
   path('handbags', views.handbags, name='handbags'),
   path('mandresses', views.mandresses, name='mandresses'),
   path('sarees', views.sarees, name='sarees'),
   path('salwarsuits', views.salwarsuits, name='salwarsuits'),
   path('scarf', views.scarf, name='scarf'),
   path('stone', views.stone, name='stone'),
   path('wallhangings', views.wallhangings, name='wallhangings'),
   path('womendresses', views.womendresses, name='womendresses'),
   path('woodenhandicraft', views.woodenhandicraft, name='woodenhandicraft'),
]
