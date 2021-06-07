from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Administratorzy)
class Administratorzy(admin.ModelAdmin):
    list_display = ("id_administratorzy","nazwisko", "imię")


@admin.register(DniTygodnia)
class DniTygodnia(admin.ModelAdmin):
    list_display = ("id_dnia_tygodnia","dzień")


@admin.register(Punkt)
class Punkt(admin.ModelAdmin):
    list_display = ("id_punktu", "nazwa")


@admin.register(Pracownicy)
class Pracownicy(admin.ModelAdmin):
    list_display = ("id_pracownika", "nazwisko", "imię")


@admin.register(GodzinyOtwarcia)
class GodzinyOtwarcia(admin.ModelAdmin):
    list_display = ("dni_tygodnia_id_dnia_tygodnia", "punkt_id_punktu")


@admin.register(Kategoria)
class Kategoria(admin.ModelAdmin):
    list_display = ("id_kategorii", "nazwa_kategorii")


@admin.register(PunktPracownicy)
class PunktPracownicy(admin.ModelAdmin):
    list_display = ("punkt_id_punktu", "pracownicy_id_pracownika")


@admin.register(Obiekt)
class Obiekt(admin.ModelAdmin):
    list_display = ("id_obiektu", "nazwa")