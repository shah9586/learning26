from django.db import models

# Create your models here.
#python class 

#parent class model
#create table student (studentName varchar(100), studentAge int, studentCity varchar(40))
# it will generate pk(id) automatically


#class Student(models.Model):
   # studentName = models.CharField(max_length=100)
    #studentAge = models.IntegerField()
    #studentCity = models.CharField(max_length=40)

    #meta class
    #class Meta:
     #   db_table = "student" #table name



class Product(models.Model):
    productName = models.CharField(max_length=100)
    productPrice = models.FloatField()
    productStock = models.IntegerField()
    productDiscount = models.FloatField(null=True)
    productColor = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = "products"


class Resturants(models.Model):
    resturantName = models.CharField(max_length=100)
    resturantLocation = models.CharField(max_length=100)
    resturantRating = models.FloatField()
    resturantType = models.CharField(max_length=50, null=True)


    class Meta:
        db_table = "resturants"

class Employee(models.Model):
    employeeName = models.CharField(max_length=100)
    employeePosition = models.CharField(max_length=100)
    employeeSalary = models.FloatField()
    employeeExperience = models.IntegerField(null=True)

    class Meta:
        db_table = "employees"