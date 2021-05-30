from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    kategorie = Kategoria.objects.all()
    context = {'kategorie':kategorie}
    return render(request, "home.html", context)


def punkty(request, id):
    kategorie = Kategoria.objects.all()
    if id is not 0:
        kategoria = Kategoria.objects.get(pk=id)
        punkty = Punkt.objects.filter(kategoria_id_kategorii=id)
    else:
        kategoria = {'nazwa_kategorii': 'Wszystko'}
        punkty = Punkt.objects.all()
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
@login_required
def panel_pracownika(request):
    return render(request, 'panel_pracownika.html')
@login_required
def pracownik_punkty(request):
    pracownik_id=request.user.id
    przypisane_punkty = PunktPracownicy.objects.filter(pracownicy_id_pracownika=1)
    punkty=[]
    for przypisany_punkt in przypisane_punkty:
        punkty.append(Punkt.objects.get(id_punktu=przypisany_punkt.punkt_id_punktu.id_punktu))
    dane = {'punkty': punkty}

    return render(request, 'pracownik_punkty.html', dane)
@login_required
def pracownik_zmiana_hasla(request):
    return render(request, 'pracownik_zmiana_hasla.html')
@login_required
def pracownik_usun_konto(request):
    return render(request, 'pracownik_usun_konto.html')
