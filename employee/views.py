from django.shortcuts import render
from .models import employees   

# Create your views here.

def employeelist(request):
    employee = employees.objects.all().values()
    print(employee)
    return render(request,"employee/employeelist.html",{"employee":employee})

def employeefilter(request):
    employee = employees.objects.filter(salary__gt=20000).values()
    print(employee)
    return render(request,"employee/employeefilter.html",{"employee":employee})
