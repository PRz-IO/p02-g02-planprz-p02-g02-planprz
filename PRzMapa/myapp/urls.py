from django.urls import path, include
from .views import *
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth.views import *
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', punkty, name='punkty'),
    path('logowanie/', logowanie, name='logowanie'),
    path('rejestracja/', rejestracja, name='rejestracja'),
    path('punkty/<int:id>/', punkt, name='punkt'),
    path('budynki/', obiekty, name='budynki'),
    path('budynki/<id>/', punkty_b, name='punkty_b'),
    path('panel-pracownika/', panel_pracownika, name='panel-pracownika'),
    path('panel-pracownika/punkty/', pracownik_punkty, name='panel-pracownika-punkty'),
    path('panel-pracownika/usun-konto/', pracownik_usun_konto, name='panel-pracownika-usun-konto'),
    path('panel-pracownika/zmiana-hasla/', pracownik_zmiana_hasla, name='panel-pracownika-zmiana-hasla'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(template_name='logowanie.html' ), name="login"),
    path('logout/', LogoutView.as_view(template_name='logowanie.html' ), name="logout"),
    url(r'^admin/', admin.site.urls),
]

