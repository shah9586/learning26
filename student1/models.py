#from curses import meta
from django.db import models

# Create your models here.
#python class 

#parent class model
#create table student (studentName varchar(100), studentAge int, studentCity varchar(40))
# it will generate pk(id) automatically



#class Student(models.Model):
 #   name = models.CharField(max_length=100)
  #  age = models.IntegerField()

   # def __str__(self):
    #    return self.name



class Student2(models.Model):
    studentName = models.CharField(max_length=100)
    studentAge = models.IntegerField()
    studentCity = models.CharField(max_length=40)

    class Meta:
        db_table = "student2"
        verbose_name_plural = "Students"
     #table name



class Product(models.Model):
    productName = models.CharField(max_length=100)
    productPrice = models.FloatField()
    productStock = models.IntegerField()
    productDiscount = models.FloatField(null=True)
    productColor = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = "products"
        verbose_name_plural = "Products"


class Restaurant(models.Model):
    resturantName = models.CharField(max_length=100)
    resturantLocation = models.CharField(max_length=100)
    resturantRating = models.FloatField()
    resturantType = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = "restaurants"
        verbose_name_plural = "Restaurants"

class Employee(models.Model):
    employeeName = models.CharField(max_length=100)
    employeePosition = models.CharField(max_length=100)
    employeeSalary = models.FloatField()
    employeeExperience = models.IntegerField(null=True)

    class Meta:
        db_table = "employees"
        verbose_name_plural = "Employees"

class StudentProfile(models.Model):
    hobbies =(("reading","reading"),("travel","travel"),("music","music"))
    #studentPrilfe id --> pk create auto...
    studentId = models.OneToOneField(Student2,on_delete=models.CASCADE)
    studentHobbies = models.CharField(max_length=100,choices=hobbies)
    studentAddress = models.CharField(max_length=100)
    studentPhone = models.CharField(max_length=10)
    studentGender = models.CharField(max_length=10)
    studentDOB = models.DateField()
    
    class Meta:
        db_table = "studentprofile"
        verbose_name_plural = "Student Profiles"

    def __str__(self):
        return self.studentId.studentName    

#cat --> #service      



#*/class Service(models.Model):
    #serviceName = models.CharField(max_length=100)
    #serviceDescription = models.TextField()
    #servicePrice = models.IntegerField()
    #serviceStatus = models.BooleanField(default=True)
    #after table creation adding new field
    #discount = models.IntegerField(null=True)
    #categoryId = models.ForeignKey('Category', on_delete=models.CASCADE)

    #class Meta:
    #    db_table = "service"
   #     verbose_name_plural = "Services"

  #  def __str__(self):
 #       return self.serviceName 

#class Category(models.Model):
   # categoryName = models.CharField(max_length=100)
    #categoryDescription = models.TextField()
    #categoryStatus = models.BooleanField(default=True)
    
   # class Meta:
      #  db_table = "category"
     #   verbose_name_plural = "Categories"

   # def __str__(self):
    #    return self.categoryName   

class Member(models.Model):
    member_name = models.CharField(max_length=100)
    
    class Meta:
     db_table = "member"
    verbose_name_plural = "Members"
    
    def __str__(self):
            return self.member_name
    
    
class MemberCard(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=20)
    
    def __str__(self):
            return self.card_number
    

class Category(models.Model):
    categoryName = models.CharField(max_length=100)

    def __str__(self):
            return self.categoryName
        

class Author(models.Model):
    author_name = models.CharField(max_length=100)

    def __str__(self):
            return self.author_name
        
class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title
    

class Issue(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField()

    from django.db import models


class Student2(models.Model):
    studentName = models.CharField(max_length=100)
    studentAge = models.IntegerField()
    studentCity = models.CharField(max_length=40)

    class Meta:
        db_table = "student2"

    def __str__(self):
        return self.studentName


class StudentProfile(models.Model):
    student = models.OneToOneField(Student2, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)

    class Meta:
        db_table = "studentprofile"

    def __str__(self):
        return self.student.studentName


# -------- One to One Example --------

class Member(models.Model):
    member_name = models.CharField(max_length=100)

    def __str__(self):
        return self.member_name


class MemberCard(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=20)

    def __str__(self):
        return self.card_number


# -------- Foreign Key Example --------

class Author(models.Model):
    author_name = models.CharField(max_length=100)

    def __str__(self):
        return self.author_name


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Issue(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
