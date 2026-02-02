from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    return HttpResponse("HELLO")

def aboutus(request):
    return render(request,"aboutus.html")

def contactus(request):
    return render(request, "contactus.html")

def home(request):
    return render(request, "home.html")

def movies(request):
    return render(request, "movies.html")

def news(request):
    return render(request, "news.html")

def recap(request):
    return render(request, "recap.html")

def recipe(request):
    ingredient =["potato,tomato,spices,bell paper, butter, onion , garlic"]
    data ={"name":"Pav bhaji", "time":10 ,"ingredient":ingredient}
    return render(request, "recipe.html",data)

def team(request):
    team_data = {
        'team_name': 'Super Kings',
        'captain': 'MS Dhoni',
        'players': ['Raina', 'Jadeja', 'hardik padya', 'boomrah'],
        'trophies': 8   
    }

    return render(request, 'team.html', team_data)

def student(request):

    marks = {
        'Maths': 70,
        'Science': 60,
        'English': 80
    }

    total = sum(marks.values())

    data = {
        'name': 'Princy',
        'marks': marks,
        'total': total
    }

    return render(request, 'student.html', data)


