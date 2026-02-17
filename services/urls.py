from django.urls import path
from . import views

urlpatterns = [
    path("", views.serviceList, name="serviceList"),
    path("create/", views.createService, name="createService"),
    path("update/<int:id>/", views.updateService, name="updateService"),
    path("delete/<int:id>/", views.deleteService, name="deleteService"),
]