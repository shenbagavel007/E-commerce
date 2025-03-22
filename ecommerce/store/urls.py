from django.urls import path
from . import views

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    
    # Authentication
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Cart Management
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),

    # Checkout
    path('checkout/', views.checkout, name='checkout'),
]
