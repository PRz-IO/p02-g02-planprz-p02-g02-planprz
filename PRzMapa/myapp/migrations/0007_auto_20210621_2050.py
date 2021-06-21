# Generated by Django 3.2.3 on 2021-06-21 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20210620_1518'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dnitygodnia',
            options={'managed': True, 'ordering': ('id', 'dzień'), 'verbose_name_plural': 'Dni tygodnia'},
        ),
        migrations.AlterModelOptions(
            name='godzinyotwarcia',
            options={'managed': True, 'ordering': ('dni_tygodnia_id_dnia_tygodnia', 'punkt_id_punktu'), 'verbose_name_plural': 'Godziny otwarcia'},
        ),
        migrations.AlterModelOptions(
            name='kategoria',
            options={'managed': True, 'ordering': ('id', 'nazwa_kategorii'), 'verbose_name_plural': 'Kategorie'},
        ),
        migrations.AlterModelOptions(
            name='obiekt',
            options={'managed': True, 'ordering': ('id', 'nazwa'), 'verbose_name_plural': 'Obiekty'},
        ),
        migrations.AlterModelOptions(
            name='pracownicy',
            options={'managed': True, 'ordering': ('id',), 'verbose_name_plural': 'Pracownicy'},
        ),
        migrations.AlterModelOptions(
            name='punkt',
            options={'managed': True, 'ordering': ('id', 'nazwa'), 'verbose_name_plural': 'Punkty'},
        ),
        migrations.AlterModelOptions(
            name='punktpracownicy',
            options={'managed': True, 'ordering': ('punkt_id_punktu', 'pracownicy_id_pracownika'), 'verbose_name_plural': 'Punkty - Pracownicy'},
        ),
        migrations.AddField(
            model_name='pracownicy',
            name='punkt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.punkt'),
        ),
        migrations.AlterField(
            model_name='dnitygodnia',
            name='dzień',
            field=models.CharField(max_length=12),
        ),
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
            field=models.EmailField(default='email@company.com', max_length=254, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='dnitygodnia',
            table='myapp_dnitygodnia',
        ),
        migrations.AlterModelTable(
            name='godzinyotwarcia',
            table='myapp_godzinyotwarcia',
        ),
        migrations.AlterModelTable(
            name='kategoria',
            table='myapp_kategoria',
        ),
        migrations.AlterModelTable(
            name='obiekt',
            table='myapp_obiekt',
        ),
        migrations.AlterModelTable(
            name='pracownicy',
            table='myapp_pracownicy',
        ),
        migrations.AlterModelTable(
            name='punkt',
            table='myapp_punkt',
        ),
        migrations.AlterModelTable(
            name='punktpracownicy',
            table='myapp_punktpracownicy',
        ),
    ]
