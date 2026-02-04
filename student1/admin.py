
from django.contrib import admin
from .models import Employee, Product,  Resturants
# Register your models here.

admin.site.register(Product)
admin.site.register(Resturants) 
admin.site.register(Employee)