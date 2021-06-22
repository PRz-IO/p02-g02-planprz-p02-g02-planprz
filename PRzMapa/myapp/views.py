from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import *


# Create your views here.

def index(request):
    kategorie = Kategoria.objects.all()
    punkty = Punkt.objects.all()
    budynki = Obiekt.objects.all()
    context = {'kategorie': kategorie,
               'punkty': punkty,
               'budynki': budynki}
    return render(request, "home.html", context)


def logowanie(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("http://127.0.0.1:8000/logowanie/")
    else:
        form=LoginForm()
#    kategorie = Kategoria.objects.all()
#    context = {'kategorie': kategorie}
    return render(request, "logowanie.html", {"form":form})


def logout(request, next_page=None, template_name='wylogowanie.html'):
    auth_logout(request)
    return render(request, "wylogowanie.html")

def rejestracja(request):
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("http://127.0.0.1:8000/")
    else:
        form=RegisterForm()
#    kategorie = Kategoria.objects.all()
#    context = {'kategorie': kategorie}
    return render(request, "rejestracja.html", {"form":form})


def punkty(request, id):
    query = request.GET.get('q')
    kategorie = Kategoria.objects.all()
    if id is not 0:
        kategoria = Kategoria.objects.get(pk=id)
        punkty = Punkt.objects.filter(Q(kategoria_id_kategorii=id), Q(nazwa__icontains=query))
    else:
        kategoria = {'nazwa_kategorii': 'Wszystkie punkty', 'id': 0}
        punkty = Punkt.objects.filter(Q(nazwa__icontains=query))

    context = {'kategoria': kategoria,
               'kategorie': kategorie,
               'punkty': punkty}
    return render(request, "punkty.html", context)


def punkt(request, id):
    kategorie = Kategoria.objects.all()
    punkt = Punkt.objects.get(pk=id)
    godzina = {'1': GodzinyOtwarcia.objects.filter(Q(punkt_id_punktu=id) & Q(dni_tygodnia_id_dnia_tygodnia=1)).first(),
               '2': GodzinyOtwarcia.objects.filter(Q(punkt_id_punktu=id) & Q(dni_tygodnia_id_dnia_tygodnia=2)).first(),
               '3': GodzinyOtwarcia.objects.filter(Q(punkt_id_punktu=id) & Q(dni_tygodnia_id_dnia_tygodnia=3)).first(),
               '4': GodzinyOtwarcia.objects.filter(Q(punkt_id_punktu=id) & Q(dni_tygodnia_id_dnia_tygodnia=4)).first(),
               '5': GodzinyOtwarcia.objects.filter(Q(punkt_id_punktu=id) & Q(dni_tygodnia_id_dnia_tygodnia=5)).first(),
               '6': GodzinyOtwarcia.objects.filter(Q(punkt_id_punktu=id) & Q(dni_tygodnia_id_dnia_tygodnia=6)).first(),
               '7': GodzinyOtwarcia.objects.filter(Q(punkt_id_punktu=id) & Q(dni_tygodnia_id_dnia_tygodnia=7)).first()}
    context = {'punkt': punkt,
               'kategorie': kategorie,
               'godzina': godzina}
    return render(request, "punkt.html", context)


def obiekty(request):
    kategorie = Kategoria.objects.all()
    query = request.GET.get('q')
    obiekty_user = Obiekt.objects.filter(Q(nazwa__icontains=query) | Q(adres__icontains=query))
    dane = {'obiekty_user': obiekty_user, 'kategorie': kategorie}
    return render(request, 'budynki.html', dane)


def punkty_b(request, id):
    kategorie = Kategoria.objects.all()
    obiekt_user = Obiekt.objects.get(pk=id)
    punkty_budynek = Punkt.objects.filter(obiekt_id_obiektu=id)
    dane = {'punkty_budynek': punkty_budynek, 'obiekt_user': obiekt_user, 'kategorie': kategorie}
    return render(request, 'budynek.html', dane)


@login_required
def panel_pracownika(request):
    pracownik = Pracownicy.objects.get(user=request.user.id)
    dane = {'pracownik': pracownik}
    return render(request, 'panel_pracownika.html', dane)


@login_required
def pracownik_punkty(request):
    user_id = request.user.id
    pracownik: Pracownicy = Pracownicy.objects.get(user=user_id)
    punkty = [pracownik.punkt]

    form = PunktForm()
    if request.method == "POST":
        form = PunktForm(request.POST, instance=pracownik.punkt)
        if form.is_valid():
            form.save()

    dane = {'punkty': punkty, "form": form}

    return render(request, 'pracownik_punkty.html', dane)


@login_required
def pracownik_usun_konto(request):
    return render(request, 'pracownik_usun_konto.html')

@login_required
def pracownik_usun_konto_potwierdzone(request):
    user_to_delete = request.user
    user_to_delete.delete()
    return redirect('index')
