from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.

def index(request):
    punkty = Punkt.objects.values('nazwa')
    context = {'nazwa':punkty}
    return render(request, "home.html", context)


def punkty(request):
    return render(request, "punkty.html")

def obiekty(request):
    query=request.GET.get('q')
    obiekty_user=Obiekt.objects.filter(Q(nazwa__icontains=query) | Q(adres__icontains=query))
    dane= {'obiekty_user': obiekty_user}
    return render(request,'budynki.html',dane)

def punkty_b(request, id):
    obiekt_user = Obiekt.objects.get(pk=id)
    punkty_budynek = Punkt.objects.filter(obiekt_id_obiektu=id)
    dane= {'punkty_budynek': punkty_budynek, 'obiekt_user': obiekt_user}
    return render(request,'budynek.html',dane)
