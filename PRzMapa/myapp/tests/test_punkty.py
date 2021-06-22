from django.test import TestCase
from ..models import *
import datetime

# Create your tests here.

class PunktTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.kategoria = Kategoria.objects.create(nazwa_kategorii='Kategoria1')

        cls.dni1 = DniTygodnia.objects.create(dzień='poniedziałek')
        cls.dni2 = DniTygodnia.objects.create(dzień='wtorek')
        cls.dni3 = DniTygodnia.objects.create(dzień='środa')
        cls.dni4 = DniTygodnia.objects.create(dzień='czwartek')
        cls.dni5 = DniTygodnia.objects.create(dzień='piątek')
        cls.dni6 = DniTygodnia.objects.create(dzień='sobota')
        cls.dni7 = DniTygodnia.objects.create(dzień='niedziela')

        cls.obiekt = Obiekt.objects.create(nazwa='Obiekt1',
                                           adres='Adres1',
                                           ułatwienia_dla_niepełnosprawnych='1',
                                           długość_geograficzna=50.245,
                                           szerokość_geograficzna=50.245)

        cls.punkt1 = Punkt.objects.create(nazwa='Punkt1',
                                          zdjęcie='www.obrazek.w.internecie.pl',
                                          obiekt_id_obiektu=Obiekt.objects.first(),
                                          informacje='tak',
                                          nr_telefonu='999999999',
                                          kategoria_id_kategorii=Kategoria.objects.first(),
                                          długość_geograficzna=50.245,
                                          szerokość_geograficzna=50.245)

        cls.user = User.objects.create(password='haslousera',
                                       username='loginusera')

        cls.prac = Pracownicy.objects.create(kontakt='999999999',
                                             czy_aktywowany='1',
                                             user=User.objects.first(),)

        cls.godz1 = GodzinyOtwarcia.objects.create(dni_tygodnia_id_dnia_tygodnia=DniTygodnia.objects.get(pk=1),
                                                   punkt_id_punktu=Punkt.objects.first(),
                                                   godz_otw='7:00',
                                                   godz_zamkn='16:00')
        cls.godz2 = GodzinyOtwarcia.objects.create(dni_tygodnia_id_dnia_tygodnia=DniTygodnia.objects.get(pk=2),
                                                   punkt_id_punktu=Punkt.objects.first(),
                                                   godz_otw='7:00',
                                                   godz_zamkn='16:00')
        cls.godz3 = GodzinyOtwarcia.objects.create(dni_tygodnia_id_dnia_tygodnia=DniTygodnia.objects.get(pk=3),
                                                   punkt_id_punktu=Punkt.objects.first(),
                                                   godz_otw='7:00',
                                                   godz_zamkn='16:00')
        cls.godz4 = GodzinyOtwarcia.objects.create(dni_tygodnia_id_dnia_tygodnia=DniTygodnia.objects.get(pk=4),
                                                   punkt_id_punktu=Punkt.objects.first(),
                                                   godz_otw='7:00',
                                                   godz_zamkn='16:00')
        cls.godz5 = GodzinyOtwarcia.objects.create(dni_tygodnia_id_dnia_tygodnia=DniTygodnia.objects.get(pk=5),
                                                   punkt_id_punktu=Punkt.objects.first(),
                                                   godz_otw='7:00',
                                                   godz_zamkn='16:00')
        cls.godz6 = GodzinyOtwarcia.objects.create(dni_tygodnia_id_dnia_tygodnia=DniTygodnia.objects.get(pk=6),
                                                   punkt_id_punktu=Punkt.objects.first(),
                                                   godz_otw='10:00',
                                                   godz_zamkn='14:00')
        cls.godz7 = GodzinyOtwarcia.objects.create(dni_tygodnia_id_dnia_tygodnia=DniTygodnia.objects.get(pk=7),
                                                   punkt_id_punktu=Punkt.objects.first(),
                                                   godz_otw='10:00',
                                                   godz_zamkn='14:00')

    def test_validacja_kategoria(self):
        temp = Kategoria.objects.get(id=1)
        self.assertEqual(temp.nazwa_kategorii, 'Kategoria1')

    def test_validacja_dnitygodnia(self):
        temp = DniTygodnia.objects.get(id=1)
        self.assertEqual(temp.dzień, 'poniedziałek')
        temp = DniTygodnia.objects.get(id=2)
        self.assertEqual(temp.dzień, 'wtorek')
        temp = DniTygodnia.objects.get(id=3)
        self.assertEqual(temp.dzień, 'środa')
        temp = DniTygodnia.objects.get(id=4)
        self.assertEqual(temp.dzień, 'czwartek')
        temp = DniTygodnia.objects.get(id=5)
        self.assertEqual(temp.dzień, 'piątek')
        temp = DniTygodnia.objects.get(id=6)
        self.assertEqual(temp.dzień, 'sobota')
        temp = DniTygodnia.objects.get(id=7)
        self.assertEqual(temp.dzień, 'niedziela')

    def test_validacja_obiekt(self):
        temp = Obiekt.objects.get(id=1)
        self.assertEqual(temp.nazwa, 'Obiekt1')
        self.assertEqual(temp.adres, 'Adres1')
        self.assertEqual(temp.ułatwienia_dla_niepełnosprawnych, '1')
        self.assertEqual(temp.długość_geograficzna, 50.245)
        self.assertEqual(temp.szerokość_geograficzna, 50.245)

    def test_validacja_punkt(self):
        temp = Punkt.objects.get(id=1)
        self.assertEqual(temp.nazwa, 'Punkt1')
        self.assertEqual(temp.zdjęcie, 'www.obrazek.w.internecie.pl')
        self.assertEqual(temp.obiekt_id_obiektu, Obiekt.objects.get(pk=1))
        self.assertEqual(temp.informacje, 'tak')
        self.assertEqual(temp.nr_telefonu, '999999999')
        self.assertEqual(temp.kategoria_id_kategorii, Kategoria.objects.get(pk=1))
        self.assertEqual(temp.długość_geograficzna, 50.245)
        self.assertEqual(temp.szerokość_geograficzna, 50.245)

    def test_validacja_user(self):
        temp = User.objects.get(id=1)
        self.assertEqual(temp.password, 'haslousera')
        self.assertEqual(temp.username, 'loginusera')

    def test_validacja_pracownicy(self):
        temp = Pracownicy.objects.get(id=1)
        self.assertEqual(temp.user, User.objects.get(pk=1))
        self.assertEqual(temp.czy_aktywowany, '1')

    def test_validacja_godziny(self):
        temp = GodzinyOtwarcia.objects.get(id=1)
        self.assertEqual(temp.dni_tygodnia_id_dnia_tygodnia, DniTygodnia.objects.get(pk=1))
        self.assertEqual(temp.punkt_id_punktu, Punkt.objects.get(pk=1))
        self.assertEqual(temp.godz_otw, datetime.time(7, 0))
        self.assertEqual(temp.godz_zamkn, datetime.time(16, 0))
        temp = GodzinyOtwarcia.objects.get(id=2)
        self.assertEqual(temp.dni_tygodnia_id_dnia_tygodnia, DniTygodnia.objects.get(pk=2))
        self.assertEqual(temp.punkt_id_punktu, Punkt.objects.get(pk=1))
        self.assertEqual(temp.godz_otw, datetime.time(7, 0))
        self.assertEqual(temp.godz_zamkn, datetime.time(16, 0))
        temp = GodzinyOtwarcia.objects.get(id=3)
        self.assertEqual(temp.dni_tygodnia_id_dnia_tygodnia, DniTygodnia.objects.get(pk=3))
        self.assertEqual(temp.punkt_id_punktu, Punkt.objects.get(pk=1))
        self.assertEqual(temp.godz_otw, datetime.time(7, 0))
        self.assertEqual(temp.godz_zamkn, datetime.time(16, 0))
        temp = GodzinyOtwarcia.objects.get(id=4)
        self.assertEqual(temp.dni_tygodnia_id_dnia_tygodnia, DniTygodnia.objects.get(pk=4))
        self.assertEqual(temp.punkt_id_punktu, Punkt.objects.get(pk=1))
        self.assertEqual(temp.godz_otw, datetime.time(7, 0))
        self.assertEqual(temp.godz_zamkn, datetime.time(16, 0))
        temp = GodzinyOtwarcia.objects.get(id=5)
        self.assertEqual(temp.dni_tygodnia_id_dnia_tygodnia, DniTygodnia.objects.get(pk=5))
        self.assertEqual(temp.punkt_id_punktu, Punkt.objects.get(pk=1))
        self.assertEqual(temp.godz_otw, datetime.time(7, 0))
        self.assertEqual(temp.godz_zamkn, datetime.time(16, 0))
        temp = GodzinyOtwarcia.objects.get(id=6)
        self.assertEqual(temp.dni_tygodnia_id_dnia_tygodnia, DniTygodnia.objects.get(pk=6))
        self.assertEqual(temp.punkt_id_punktu, Punkt.objects.get(pk=1))
        self.assertEqual(temp.godz_otw, datetime.time(10, 0))
        self.assertEqual(temp.godz_zamkn, datetime.time(14, 0))
        temp = GodzinyOtwarcia.objects.get(id=7)
        self.assertEqual(temp.dni_tygodnia_id_dnia_tygodnia, DniTygodnia.objects.get(pk=7))
        self.assertEqual(temp.punkt_id_punktu, Punkt.objects.get(pk=1))
        self.assertEqual(temp.godz_otw, datetime.time(10, 0))
        self.assertEqual(temp.godz_zamkn, datetime.time(14, 0))