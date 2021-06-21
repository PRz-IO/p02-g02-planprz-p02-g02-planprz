from django.test import TestCase
from ..models import *

# Create your tests here.

class PunktTest(TestCase):
    def setUp(self):
        Kategoria.objects.create(nazwa_kategorii='Kategoria1')

        DniTygodnia.objects.create(dzień='poniedziałek')
        DniTygodnia.objects.create(dzień='wtorek')
        DniTygodnia.objects.create(dzień='środa')
        DniTygodnia.objects.create(dzień='czwartek')
        DniTygodnia.objects.create(dzień='piątek')
        DniTygodnia.objects.create(dzień='sobota')
        DniTygodnia.objects.create(dzień='niedziela')

        Obiekt.objects.create(nazwa='Obiekt1',
                              adres='Adres1',
                              ułatwienia_dla_niepełnosprawnych='1',
                              długość_geograficzna=50.245,
                              szerokość_geograficzna=50.245)

        Punkt.objects.create(nazwa='Punkt1',
                             zdjęcie='www.obrazek.w.internecie.pl',
                             obiekt_id_obiektu=1,
                             informacje='tak',
                             nr_telefonu='999999999',
                             kategoria_id_kategorii=1,
                             długość_geograficzna=50.245,
                             szerokość_geograficzna=50.245)

        Punkt.objects.create(nazwa='Punkt2',
                             obiekt_id_obiektu=1,
                             kategoria_id_kategorii=1,
                             długość_geograficzna=50.245,
                             szerokość_geograficzna=50.245)

        User.objects.create(password='haslousera',
                            username='loginusera')

        Pracownicy.objects.create(user=1,
                                  kontakt='999999999',
                                  czy_aktywowany='1',
                                  punkt=1)

        GodzinyOtwarcia.objects.create(dni_tygodnia_id_dnia_tygodnia=1,
                                       punkt_id_punktu=1,
                                       godz_otw='7:00',
                                       godz_zamkn='16:00')
        GodzinyOtwarcia.objects.create(dni_tygodnia_id_dnia_tygodnia=2,
                                       punkt_id_punktu=1,
                                       godz_otw='7:00',
                                       godz_zamkn='16:00')
        GodzinyOtwarcia.objects.create(dni_tygodnia_id_dnia_tygodnia=3,
                                       punkt_id_punktu=1,
                                       godz_otw='7:00',
                                       godz_zamkn='16:00')
        GodzinyOtwarcia.objects.create(dni_tygodnia_id_dnia_tygodnia=4,
                                       punkt_id_punktu=1,
                                       godz_otw='7:00',
                                       godz_zamkn='16:00')
        GodzinyOtwarcia.objects.create(dni_tygodnia_id_dnia_tygodnia=5,
                                       punkt_id_punktu=1,
                                       godz_otw='7:00',
                                       godz_zamkn='16:00')
        GodzinyOtwarcia.objects.create(dni_tygodnia_id_dnia_tygodnia=6,
                                       punkt_id_punktu=1,
                                       godz_otw='10:00',
                                       godz_zamkn='14:00')
        GodzinyOtwarcia.objects.create(dni_tygodnia_id_dnia_tygodnia=7,
                                       punkt_id_punktu=1,
                                       godz_otw='10:00',
                                       godz_zamkn='14:00')

    def test_validacja(self):
        temp = Punkt.objects.get(id=1)
        self.assertEqual(temp.nazwa, 'Punkt1')
        self.assertEqual(temp.zdjęcie, 'www.obrazek.w.internecie.pl')
        self.assertEqual(temp.obiekt_id_obiektu, 1)
        self.assertEqual(temp.informacje, 'tak')
        self.assertEqual(temp.nr_telefonu, '999999999')
        self.assertEqual(temp.kategoria_id_kategorii, 1)
        self.assertEqual(temp.długość_geograficzna, 50.245)
        self.assertEqual(temp.szerokość_geograficzna, 50.245)

        temp = Punkt.objects.get(id=2)
        self.assertEqual(temp.nazwa, 'Punkt2')
        self.assertEqual(temp.obiekt_id_obiektu, 1)
        self.assertEqual(temp.kategoria_id_kategorii, 1)
        self.assertEqual(temp.długość_geograficzna, 50.245)
        self.assertEqual(temp.szerokość_geograficzna, 50.245)

        temp = Kategoria.objects.get(id=1)
        self.assertEqual(temp.nazwa, 'Kategoria1')

        temp = DniTygodnia.objects.get(id=1)
        self.assertEqual(temp.dzień, 'poniedziałek')

        temp = Obiekt.objects.get(id=1)
        self.assertEqual(temp.nazwa, 'Obiekt1')
        self.assertEqual(temp.adres, 'Adres1')
        self.assertEqual(temp.ułatwienia_dla_niepełnosprawnych, '1')
        self.assertEqual(temp.długość_geograficzna, 50.245)
        self.assertEqual(temp.szerokość_geograficzna, 50.245)

        temp = User.objects.get(id=1)
        self.assertEqual(temp.password, 'haslousera')
        self.assertEqual(temp.username, 'loginusera')

        temp = Pracownicy.objects.get(id=1)
        self.assertEqual(temp.user, 1)
        self.assertEqual(temp.kontakt, '999999999')
        self.assertEqual(temp.czy_aktywowany, '1')
        self.assertEqual(temp.punkt, 1)

        temp = GodzinyOtwarcia.objects.get(id=1)
        self.assertEqual(temp.dni_tygodnia_id_dnia_tygodnia, 1)
        self.assertEqual(temp.punkt_id_punktu, 1)
        self.assertEqual(temp.godz_otw, '10:00')
        self.assertEqual(temp.godz_zamkn, '14:00')
