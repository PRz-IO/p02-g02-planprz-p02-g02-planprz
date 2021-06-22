from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Pracownicy
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def create_pracownik(sender, instance: User, created, **kwargs):
    if created:
        if not instance.is_superuser:  # Jesli user nie jest adminem to stworz Pracownika
            Pracownicy.objects.create(user=instance, kontakt=instance.email, czy_aktywowany='1', punkt=None)
