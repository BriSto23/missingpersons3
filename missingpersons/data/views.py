# Missing Persons Group Project
# Garrett Ashcroft, Charlotte Griffin, Brian Stone, Andrew Hunsaker, Amy Dutson, Preston Vance

from django.shortcuts import render
from django.http import HttpResponse
from .models import MissingPerson

# Create your views here.

def indexPageView(request) :
    return render(request, 'data/index.html')

def dataPageView(request):
    data = MissingPerson.objects.all()

    context = {
        'person' : data
    }
    return render(request, 'data/data.html', context)

def learnPageView(request, id) :
    data = MissingPerson.objects.get(last_name = id)

    context = {
        "record" : data,
        
    }
    return render(request, 'data/learn.html', context)