from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', punkty, name='punkty'),
    path('punkty/<int:id>/', punkt, name='punkt'),
    path('budynki/', obiekty, name='budynki'),
    path('budynki/<id>/', punkty_b, name='punkty_b'),
]

