from django.test import TestCase
from ..models import *

# Create your tests here.

class PunktTest(TestCase):
    def setUp(self):
        Punkt.objects.create(id_punktu=1,
                             nazwa='Testowa965',
                             zdjęcie='www.google.pl',
                             obiekt_id_obiektu=1,
                             informacje='tak',
                             nr_telefonu='999999999',
                             kategoria_id_kategorii=1,
                             długość_geograficzna= 50.245,
                             szerokość_geograficzna= 50.245)

    def test_punkt_validation(self):
        one = Punkt.objects.get(id_punktu=1)
        self.assertEqual(one.informacje, 'tak')
