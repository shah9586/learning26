from django.shortcuts import render, redirect
from .form import ServiceForm
from .models import Services

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
    services = Services.objects.all().order_by("id").values() #select * from services order by id       
    return render(request, "services/serviceList.html", {"services": services})

def updateService(request, id):
    service = Services.objects.get(id=id)

    if request.method == "POST":
       # Services = Services.objects.get(id=id).order_by(id).value() #select * from services where id = 1
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect("serviceList")
    else:
        form = ServiceForm(instance=service)

    return render(request, "services/createService.html", {"form": form})

def deleteService(request, id):
    service = Services.objects.get(id=id)
    service.delete()
    return redirect("serviceList")

