# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administratorzy(models.Model):
    id_administratorzy = models.AutoField(primary_key=True)
    nazwisko = models.CharField(max_length=40)
    imię = models.CharField(max_length=40)
    adres_mailowy = models.CharField(max_length=40)
    hasło = models.CharField(max_length=20)
    nr_telefonu = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'administratorzy'


class DniTygodnia(models.Model):
    id_dnia_tygodnia = models.AutoField(primary_key=True)
    dzień = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'dni_tygodnia'


class GodzinyOtwarcia(models.Model):
    dni_tygodnia_id_dnia_tygodnia = models.ForeignKey(DniTygodnia, models.DO_NOTHING, db_column='dni_tygodnia_id_dnia_tygodnia')
    punkt_id_punktu = models.ForeignKey('Punkt', models.DO_NOTHING, db_column='punkt_id_punktu')
    godz_otw = models.TimeField()
    godz_zamkn = models.TimeField()

    class Meta:
        managed = False
        db_table = 'godziny_otwarcia'


class Kategoria(models.Model):
    id_kategorii = models.AutoField(primary_key=True)
    nazwa_kategorii = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'kategoria'


class Obiekt(models.Model):
    id_obiektu = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=40)
    adres = models.CharField(max_length=40)
    ułatwienia_dla_niepełnosprawnych = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'obiekt'


class Pracownicy(models.Model):
    id_pracownika = models.AutoField(primary_key=True)
    imię = models.CharField(max_length=40)
    nazwisko = models.CharField(max_length=40)
    adres_mailowy = models.CharField(max_length=40)
    hasło = models.CharField(max_length=20)
    kontakt = models.CharField(max_length=40, blank=True, null=True)
    data_założenia_konta = models.DateField()
    czy_aktywowany = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'pracownicy'


class Punkt(models.Model):
    id_punktu = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=40)
    zdjęcie = models.TextField(blank=True, null=True)
    obiekt_id_obiektu = models.ForeignKey(Obiekt, models.DO_NOTHING, db_column='obiekt_id_obiektu')
    informacje = models.CharField(max_length=50, blank=True, null=True)
    nr_telefonu = models.CharField(max_length=9, blank=True, null=True)
    kategoria_id_kategorii = models.ForeignKey(Kategoria, models.DO_NOTHING, db_column='kategoria_id_kategorii')
    długość_geograficzna = models.FloatField()
    szerokość_geograficzna = models.FloatField()

    class Meta:
        managed = False
        db_table = 'punkt'


class PunktPracownicy(models.Model):
    punkt_id_punktu = models.ForeignKey(Punkt, models.DO_NOTHING, db_column='punkt_id_punktu')
    pracownicy_id_pracownika = models.ForeignKey(Pracownicy, models.DO_NOTHING, db_column='pracownicy_id_pracownika')

    class Meta:
        managed = False
        db_table = 'punkt_pracownicy'
