from django.shortcuts import render


# Create your views here.
def studentdetails(request):
    details = {"name" : "Princy" ,
                "age":21, 
                "contact":9876543210
              }
    return render(request,"student1/studentdetail.html",details)

def studentmarks(request):
    marks = { "Maths" : 83 , 
             "Science" : 76,
             "English" : 89 
    }
    return render(request,"student1/studentmarks.html",marks)

def studentresult(request):
    Maths = 83
    Science = 76
    English = 89

    total = Maths + Science + English
    percentage = (total / 300) * 100
    
    if percentage >= 80:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "Fail"
    
    result = {
        "Maths": Maths, 
        "Science": Science,
        "English": English,  

        "Total": total,
        "Percentage": percentage,  
        "Result": "Pass" if percentage >= 40 else "Fail",
        "grade": grade
    }
    return render(request,"student1/studentresult.html",result)