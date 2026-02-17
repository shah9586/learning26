from django.urls import path
from . import views

urlpatterns = [
    path("", views.serviceList, name="serviceList"),
    path("create/", views.createService, name="createService"),
    path("edit/<int:id>/", views.editService, name="editService"),
    path("delete/<int:id>/", views.deleteService, name="deleteService"),
]