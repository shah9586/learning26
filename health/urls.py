from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('scan/', views.scan_product, name='scan_product'),
    path('rewards/', views.my_rewards, name='my_rewards'),
]
