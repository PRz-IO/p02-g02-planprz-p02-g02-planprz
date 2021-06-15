# Generated by Django 3.2.3 on 2021-06-15 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20210615_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obiekt',
            name='ułatwienia_dla_niepełnosprawnych',
            field=models.CharField(choices=[('0', 'nie'), ('1', 'tak')], max_length=10, verbose_name='Ułatwienia dla niepełnosprawnych'),
        ),
        migrations.AlterField(
            model_name='pracownicy',
            name='czy_aktywowany',
            field=models.CharField(choices=[('0', 'nie'), ('1', 'tak')], max_length=10, verbose_name='Czy aktywowany'),
        ),
    ]
