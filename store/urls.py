from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name='home'),
    path("contact", views.contact,name='contact'),
    path("about", views.about,name='about'),
    path("cart", views.cart,name='cart'),
    path("payment", views.payment,name='payment'),
   
]
