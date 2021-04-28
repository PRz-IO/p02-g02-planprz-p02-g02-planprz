# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administratorzy(models.Model):
    id_administratorzy = models.IntegerField(primary_key=True)
    nazwisko = models.CharField(max_length=40)
    imię = models.CharField(max_length=40)
    adres_mailowy = models.CharField(max_length=40)
    hasło = models.CharField(max_length=20)
    nr_telefonu = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'administratorzy'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DniTygodnia(models.Model):
    id_dnia_tygodnia = models.IntegerField(primary_key=True)
    dzień = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'dni_tygodnia'


class GodzinyOtwarcia(models.Model):
    punkt_id_punktu = models.ForeignKey('Punkt', models.DO_NOTHING, db_column='punkt_id_punktu')
    godz_otw = models.TimeField()
    godz_zamkn = models.TimeField()
    id_dnia_tygodnia = models.ForeignKey(DniTygodnia, models.DO_NOTHING, db_column='id_dnia_tygodnia')

    class Meta:
        managed = False
        db_table = 'godziny_otwarcia'


class Kategoria(models.Model):
    id_kategorii = models.IntegerField(primary_key=True)
    nazwa_kategorii = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'kategoria'


class Obiekt(models.Model):
    id_obiektu = models.IntegerField(primary_key=True)
    nazwa = models.CharField(max_length=40)
    adres = models.CharField(max_length=40)
    ułatwienia_dla_niepełnosprawnych = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'obiekt'


class Pracownicy(models.Model):
    id_pracownika = models.IntegerField(primary_key=True)
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
    id_punktu = models.IntegerField(primary_key=True)
    nazwa = models.CharField(max_length=40)
    kategoria = models.IntegerField()
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
