from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def home(request):
    people = [
    {'name': 'Abhijeet Gupta', 'age': 26},
    {'name': 'Rohan Sharma', 'age': 23},
    {'name': 'Vicky Kaushal', 'age': 17},
    {'name': 'DeepanShu Chaurasiya', 'age': 16},
    {'name': 'Sandeep', 'age': 63}
]
    return render(request,"index.html",context={'peoples':people,"page":"Home page"})

def contact(request):
    page="Contact page"
    return render(request,"contact.html",context={"page":page})

def about(request):
    page="about page"
    return render(request,"about.html",context={"page":page})
