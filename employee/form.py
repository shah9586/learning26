from django import forms
from .models import Employee, Course


# Employee Form
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


# Course Form
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
