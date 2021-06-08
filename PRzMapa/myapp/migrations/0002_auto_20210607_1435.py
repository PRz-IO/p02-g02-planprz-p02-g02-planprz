# Generated by Django 3.2.3 on 2021-06-07 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='administratorzy',
            options={'managed': True, 'verbose_name_plural': 'Administratorzy'},
        ),
        migrations.AlterModelOptions(
            name='dnitygodnia',
            options={'managed': True, 'verbose_name_plural': 'Dni tygodnia'},
        ),
        migrations.AlterModelOptions(
            name='godzinyotwarcia',
            options={'managed': True, 'verbose_name_plural': 'Godziny otwarcia'},
        ),
        migrations.AlterModelOptions(
            name='kategoria',
            options={'managed': True, 'verbose_name_plural': 'Kategorie'},
        ),
        migrations.AlterModelOptions(
            name='obiekt',
            options={'managed': True, 'verbose_name_plural': 'Obiekty'},
        ),
        migrations.AlterModelOptions(
            name='pracownicy',
            options={'managed': True, 'verbose_name_plural': 'Pracownicy'},
        ),
        migrations.AlterModelOptions(
            name='punkt',
            options={'managed': True, 'verbose_name_plural': 'Punkty'},
        ),
        migrations.AlterModelOptions(
            name='punktpracownicy',
            options={'managed': True, 'verbose_name_plural': 'Punkty - Pracownicy'},
        ),
    ]
