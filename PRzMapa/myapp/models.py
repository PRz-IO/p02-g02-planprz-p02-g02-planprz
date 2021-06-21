# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

wybory = {
    ('0', 'nie'),
    ('1', 'tak')
}

# class Administratorzy(models.Model):
#     id_administratorzy = models.AutoField(primary_key=True)
#     nazwisko = models.CharField(max_length=40)
#     imię = models.CharField(max_length=40)
#     adres_mailowy = models.CharField(max_length=40, verbose_name="Adres e-mail")
#     hasło = models.CharField(max_length=20)
#     nr_telefonu = models.CharField(max_length=9, blank=True, null=True, verbose_name="Telefon")
#
#     def __str__(self):
#         return f"{self.id_administratorzy}, {self.nazwisko} {self.imię}"
#
#     class Meta:
#         managed = True
#         db_table = 'administratorzy'
#         verbose_name_plural = "Administratorzy"
#         ordering = ("id_administratorzy","nazwisko", "imię")


class DniTygodnia(models.Model):
 #   id_dnia_tygodnia = models.AutoField(primary_key=True)
    dzień = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.id}, {self.dzień}"

    class Meta:
        managed = True
        db_table = 'myapp_dnitygodnia'
        verbose_name_plural = "Dni tygodnia"
        ordering = ("id","dzień")


class GodzinyOtwarcia(models.Model):
    dni_tygodnia_id_dnia_tygodnia = models.ForeignKey(DniTygodnia, models.DO_NOTHING, null=True, db_column='dni_tygodnia_id_dnia_tygodnia', verbose_name="Dzień tygodnia")
    punkt_id_punktu = models.ForeignKey('Punkt', models.DO_NOTHING, null=True, db_column='punkt_id_punktu', verbose_name="Nazwa punktu")
    godz_otw = models.TimeField(verbose_name='Godzina otwarcia', help_text="Wprowadź godzinę od 00:00 do 23:59")
    godz_zamkn = models.TimeField(verbose_name='Godzina zamknięcia', help_text="Wprowadź godzinę od 00:00 do 23:59")

    def __str__(self):
        return f"{self.dni_tygodnia_id_dnia_tygodnia}, {self.punkt_id_punktu}"

    class Meta:
        managed = True
        db_table = 'myapp_godzinyotwarcia'
        verbose_name_plural = "Godziny otwarcia"
        ordering = ("dni_tygodnia_id_dnia_tygodnia", "punkt_id_punktu")

class Kategoria(models.Model):
 #   id_kategorii = models.AutoField(primary_key=True)
    nazwa_kategorii = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id}, {self.nazwa_kategorii}"

    class Meta:
        managed = True
        db_table = 'myapp_kategoria'
        verbose_name_plural = "Kategorie"
        ordering = ("id", "nazwa_kategorii")


class Obiekt(models.Model):
 #   id_obiektu = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=40)
    adres = models.CharField(max_length=40)
    ułatwienia_dla_niepełnosprawnych = models.CharField(max_length=10, choices=wybory, verbose_name="Ułatwienia dla niepełnosprawnych")
    długość_geograficzna = models.FloatField()
    szerokość_geograficzna = models.FloatField()

    def __str__(self):
        return f"{self.id}, {self.nazwa}"

    class Meta:
        managed = True
        db_table = 'myapp_obiekt'
        verbose_name_plural = "Obiekty"
        ordering = ("id", "nazwa")



class Punkt(models.Model):
 #   id_punktu = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=40)
    zdjęcie = models.TextField(blank=True, null=True, db_column='zdjęcie')
    obiekt_id_obiektu = models.ForeignKey(Obiekt, models.DO_NOTHING, db_column='obiekt_id_obiektu', verbose_name="Nazwa obiektu")
    informacje = models.CharField(max_length=50, blank=True, null=True)
    nr_telefonu = models.CharField(max_length=9, blank=True, null=True, verbose_name="Telefon")
    kategoria_id_kategorii = models.ForeignKey(Kategoria, models.DO_NOTHING, db_column='kategoria_id_kategorii', verbose_name="Kategoria")
    długość_geograficzna = models.FloatField()
    szerokość_geograficzna = models.FloatField()

    def __str__(self):
        return f"{self.id}, {self.nazwa}"

    class Meta:
        managed = True
        db_table = 'myapp_punkt'
        verbose_name_plural = "Punkty"
        ordering = ("id", "nazwa")


class Pracownicy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kontakt = models.EmailField(verbose_name="Email")
    czy_aktywowany = models.CharField(max_length=10, choices=wybory, verbose_name="Czy aktywny")

    def __str__(self):
        return f"{self.id}, {self.user.first_name} {self.user.last_name}"

    class Meta:
        managed = True
        db_table = 'myapp_pracownicy'
        verbose_name_plural = "Pracownicy"
        ordering = ("id",)


class PunktPracownicy(models.Model):
 #   id = models.AutoField(primary_key=True, db_column='id')
    punkt_id_punktu = models.ForeignKey(Punkt, models.DO_NOTHING, db_column='punkt_id_punktu', verbose_name="Nazwa punktu")
    pracownicy_id_pracownika = models.ForeignKey(Pracownicy, models.DO_NOTHING, db_column='pracownicy_id_pracownika', verbose_name="Pracownik")

    def __str__(self):
        return f"{self.punkt_id_punktu}, {self.pracownicy_id_pracownika}"

    class Meta:
        managed = True
        db_table = 'myapp_punktpracownicy'
        verbose_name_plural = "Punkty - Pracownicy"
        ordering = ("punkt_id_punktu", "pracownicy_id_pracownika")
