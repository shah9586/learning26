from django.urls import path
from . import views

urlpatterns = [
    path('details/',views.studentdetails),
    path('marks/',views.studentmarks),
    path('result/',views.studentresult),
]
