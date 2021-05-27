from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('budynki/', obiekty, name='budynki'),
    path('punkty/', punkty, name='punkty'),
    path('budynki/<id>/', punkty_b, name='punkty_b'),

]

