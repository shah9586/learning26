from django.shortcuts import render, redirect
from .form import ServiceForm
from .models import Service

def createService(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("serviceList")
    else:
        form = ServiceForm()

    return render(request, "services/createService.html", {"form": form})

def serviceList(request):
    services = Service.objects.all()
    return render(request, "services/serviceList.html", {"services": services})

def updateService(request, id):
    service = Service.objects.get(id=id)

    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect("serviceList")
    else:
        form = ServiceForm(instance=service)

    return render(request, "services/createService.html", {"form": form})

def deleteService(request, id):
    service = Service.objects.get(id=id)
    service.delete()
    return redirect("serviceList")

