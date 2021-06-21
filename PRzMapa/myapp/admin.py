from .models import *
from django.contrib.auth.models import User, Group
from django.contrib import admin
#
# # Register your models here.
# #admin.site.unregister(User)
# #admin.site.unregister(Group)
#
#
# class AdministratorzyAdmin(admin.ModelAdmin):
#     list_display = ('id_administratorzy','Nazwisko_i_imię','adres_mailowy','nr_telefonu')
#     search_fields = ('imię', 'nazwisko', 'adres_mailowy', 'nr_telefonu')
#
#     def Nazwisko_i_imię(self, obj):
#         return "{} {}".format(obj.nazwisko, obj.imię)
#
#


class DniTygodniaAdmin(admin.ModelAdmin):
    list_display = ("id","dzień")

    def has_add_permission(self, request, obj=None):
        return False


class InLineGodzinyOtwarcia(admin.StackedInline):
    model = GodzinyOtwarcia
    max_num = 7


class PunktAdmin(admin.ModelAdmin):
    inlines = [InLineGodzinyOtwarcia]
    list_display = ("id", "nazwa")
    list_filter = ('kategoria_id_kategorii',)
    search_fields = ('nazwa', 'informacje')


class PracownicyAdmin(admin.ModelAdmin):
    list_display = ("id",'Nazwisko_i_imię', 'kontakt', 'czy_aktywowany')
    #TODO: naprawić search_field bo sypie błędy
    #search_fields = ('user','kontakt')
    list_filter = ('czy_aktywowany',)

    def Nazwisko_i_imię(self, obj):
        return "{} {}".format(obj.user.last_name, obj.user.first_name)


class GodzinyOtwarciaAdmin(admin.ModelAdmin):
    list_display = ("dni_tygodnia_id_dnia_tygodnia", "punkt_id_punktu")
    list_filter = ('dni_tygodnia_id_dnia_tygodnia',)
    fields = ('dni_tygodnia_id_dnia_tygodnia', 'punkt_id_punktu', ('godz_otw', 'godz_zamkn'))


class KategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nazwa_kategorii")
    list_filter = ('nazwa_kategorii',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class PunktPracownicyAdmin(admin.ModelAdmin):
    list_display = ("punkt_id_punktu", "pracownicy_id_pracownika")
    list_filter = ('punkt_id_punktu', 'pracownicy_id_pracownika')


class ObiektAdmin(admin.ModelAdmin):
    list_display = ("id", "nazwa",'adres','ułatwienia_dla_niepełnosprawnych')
    list_filter = ('ułatwienia_dla_niepełnosprawnych',)
    search_fields = ('nazwa', 'adres')


#admin.site.register(Administratorzy)
admin.site.register(DniTygodnia, DniTygodniaAdmin)
admin.site.register(Punkt, PunktAdmin)
admin.site.register(Pracownicy, PracownicyAdmin)
admin.site.register(GodzinyOtwarcia, GodzinyOtwarciaAdmin)
admin.site.register(Kategoria, KategoriaAdmin)
admin.site.register(PunktPracownicy, PunktPracownicyAdmin)
admin.site.register(Obiekt, ObiektAdmin)
