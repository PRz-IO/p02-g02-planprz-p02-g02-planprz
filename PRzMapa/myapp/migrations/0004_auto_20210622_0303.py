# Generated by Django 3.2.4 on 2021-06-22 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_pracownicy_kontakt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obiekt',
            name='ułatwienia_dla_niepełnosprawnych',
            field=models.CharField(choices=[('1', 'tak'), ('0', 'nie')], max_length=10, verbose_name='Ułatwienia dla niepełnosprawnych'),
        ),
        migrations.AlterField(
            model_name='pracownicy',
            name='czy_aktywowany',
            field=models.CharField(choices=[('1', 'tak'), ('0', 'nie')], max_length=10, verbose_name='Czy aktywny'),
        ),
        migrations.AlterField(
            model_name='pracownicy',
            name='kontakt',
            field=models.CharField(default=4, max_length=9, verbose_name='Telefon'),
            preserve_default=False,
        ),
    ]