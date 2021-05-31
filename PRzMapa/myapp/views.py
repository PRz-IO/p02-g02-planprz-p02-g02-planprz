from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.

def index(request):
    kategorie = Kategoria.objects.all()
    context = {'kategorie':kategorie}
    return render(request, "home.html", context)

def logowanie(request):
    kategorie = Kategoria.objects.all()
    context = {'kategorie': kategorie}
    return render(request, "logowanie.html", context)

def punkty(request, id):
    query = request.GET.get('q')
    kategorie = Kategoria.objects.all()
    if id is not 0:
        kategoria = Kategoria.objects.get(pk=id)
        punkty = Punkt.objects.filter(Q(kategoria_id_kategorii=id), Q(nazwa__icontains=query))
    else:
        kategoria = {'nazwa_kategorii': 'Wszystko', 'id_kategorii': 0}
        punkty = Punkt.objects.filter(Q(nazwa__icontains=query))

    context = {'kategoria': kategoria,
               'kategorie': kategorie,
               'punkty': punkty}
    return render(request, "punkty.html", context)

def punkt(request , id):
    kategorie = Kategoria.objects.all()
    punkt = Kategoria.objects.get(pk=id)
    context = {'punkt': punkt, 'kategorie':kategorie}
    return render(request, "punkt.html", context)

def obiekty(request):
    kategorie = Kategoria.objects.all()
    query=request.GET.get('q')
    obiekty_user=Obiekt.objects.filter(Q(nazwa__icontains=query) | Q(adres__icontains=query))
    dane= {'obiekty_user': obiekty_user, 'kategorie':kategorie}
    return render(request,'budynki.html',dane)

def punkty_b(request, id):
    kategorie = Kategoria.objects.all()
    obiekt_user = Obiekt.objects.get(pk=id)
    punkty_budynek = Punkt.objects.filter(obiekt_id_obiektu=id)
    dane= {'punkty_budynek': punkty_budynek, 'obiekt_user': obiekt_user, 'kategorie':kategorie}
    return render(request,'budynek.html',dane)
