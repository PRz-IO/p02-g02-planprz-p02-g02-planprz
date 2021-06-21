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
    path('panel-pracownika/punkty/', pracownik_punkty, name='panel-pracownika-punkty'),
    path('panel-pracownika/usun-konto/', pracownik_usun_konto, name='panel-pracownika-usun-konto'),
    path('panel-pracownika/usun-konto/potwierdzone/', pracownik_usun_konto_potwierdzone,
         name='panel-pracownika-usun-konto-potwierdzone'),
    path('panel-pracownika/zmiana-hasla/', PasswordChangeView.as_view(template_name="myapp/pracownik_zmiana_hasla.html",
                                                                      success_url=reverse_lazy("panel-pracownika")),
         name='panel-pracownika-zmiana-hasla'),
    path('panel-pracownika/', panel_pracownika, name='panel-pracownika'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(template_name='logowanie.html' ), name="login"),
    path('logout/', LogoutView.as_view(template_name='wylogowanie.html' ), name="logout"),
    url(r'^admin/', admin.site.urls),
]

