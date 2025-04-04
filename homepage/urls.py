from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('cart/', views.cart, name='cart'),
    path('productdetails/', views.productdetails, name='productdetails'),
    path('checkout1/', views.checkout1, name='checkout1'),
    path('checkout2/', views.checkout2, name='checkout2'),
    path('checkout3', views.checkout3, name='checkout3'),
]