from . import views
from django.urls import path
urlpatterns = [
    path('employeelist/',views.employeelist,name="employeelist"),
    path('employeefilter/',views.employeefilter,name="employeefilter"),   
]