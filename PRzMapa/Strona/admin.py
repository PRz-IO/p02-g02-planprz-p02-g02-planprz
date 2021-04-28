from django.contrib import admin
from .models import *

from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register(Administratorzy)
admin.site.register(Punkt)
admin.site.register(Pracownicy)
admin.site.register(DniTygodnia)
admin.site.register(GodzinyOtwarcia)
admin.site.register(Kategoria)
admin.site.register(PunktPracownicy)
admin.site.register(Obiekt)

admin.site.unregister(User)
admin.site.unregister(Group)