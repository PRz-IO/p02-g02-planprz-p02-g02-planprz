from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    punkty = Punkt.objects.values('nazwa')
    context = {'nazwa':punkty}
    return render(request, "home.html", context)


def budynki(request):
    return render(request, "budynki.html")