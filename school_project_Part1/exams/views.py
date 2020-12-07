from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    name = "Billy"
    age = -99

    context = {
        "name": name, 
        "age": age,
        "fav_food": ["Hamburgers", "Pizza", "Streetcat Kebabs"]
    }
    

    return render(request, 'home.html', context)

def dashboard(request):
    return render(request, 'dashboard.html')



def students(request):
    names = ["Jon", "Bob", "Timmy", "Tommy", "Tali"]
    return render(request, 'students.html', {"people": names})