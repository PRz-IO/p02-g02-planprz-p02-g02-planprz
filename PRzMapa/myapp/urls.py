from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', punkty, name='punkty'),
    path('punkty/<int:id>/', punkt, name='punkt'),
    path('budynki/', obiekty, name='budynki'),
    path('budynki/<id>/', punkty_b, name='punkty_b'),
    path('panel-pracownika/', panel_pracownika, name='panel-pracownika'),
    path('panel-pracownika/punkty/', pracownik_punkty, name='panel-pracownika-punkty'),
    path('panel-pracownika/usun-konto/', pracownik_usun_konto, name='panel-pracownika-usun-konto'),
    path('panel-pracownika/zmiana-hasla/', pracownik_zmiana_hasla, name='panel-pracownika-zmiana-hasla')

]

