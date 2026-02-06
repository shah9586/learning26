
from django.contrib import admin
from .models import Employee, Product,  Resturants, StudentProfile, Category,Service, Student2, Member, MemberCard , Book, Author        
# Register your models here.

admin.site.register(Product)
admin.site.register(Resturants) 
admin.site.register(Employee)
admin.site.register(Member)
admin.site.register(MemberCard)     
admin.site.register(StudentProfile)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Student2)
admin.site.register(Author)
admin.site.register(Book)

