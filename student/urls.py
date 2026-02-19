from django.urls import path
from . import views

urlpatterns = [
   path("home/",views.studentHome),
   path("dashboard/",views.studentDashboard),
    path("servicelist/",views.servicelist,name="servicelist"),
   path("createservice/",views.createService,name="createservice"),
]