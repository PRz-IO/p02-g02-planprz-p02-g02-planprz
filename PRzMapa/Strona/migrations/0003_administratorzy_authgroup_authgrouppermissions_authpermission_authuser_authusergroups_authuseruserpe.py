# Generated by Django 3.2 on 2021-04-28 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Strona', '0002_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administratorzy',
            fields=[
                ('id_administratorzy', models.IntegerField(primary_key=True, serialize=False)),
                ('nazwisko', models.CharField(max_length=40)),
                ('imię', models.CharField(max_length=40)),
                ('adres_mailowy', models.CharField(max_length=40)),
                ('hasło', models.CharField(max_length=20)),
                ('nr_telefonu', models.CharField(blank=True, max_length=9, null=True)),
            ],
            options={
                'db_table': 'administratorzy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DniTygodnia',
            fields=[
                ('id_dnia_tygodnia', models.IntegerField(primary_key=True, serialize=False)),
                ('dzień', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'dni_tygodnia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GodzinyOtwarcia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('godz_otw', models.TimeField()),
                ('godz_zamkn', models.TimeField()),
            ],
            options={
                'db_table': 'godziny_otwarcia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('id_kategorii', models.IntegerField(primary_key=True, serialize=False)),
                ('nazwa_kategorii', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'kategoria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Obiekt',
            fields=[
                ('id_obiektu', models.IntegerField(primary_key=True, serialize=False)),
                ('nazwa', models.CharField(max_length=40)),
                ('adres', models.CharField(max_length=40)),
                ('ułatwienia_dla_niepełnosprawnych', models.TextField()),
            ],
            options={
                'db_table': 'obiekt',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pracownicy',
            fields=[
                ('id_pracownika', models.IntegerField(primary_key=True, serialize=False)),
                ('imię', models.CharField(max_length=40)),
                ('nazwisko', models.CharField(max_length=40)),
                ('adres_mailowy', models.CharField(max_length=40)),
                ('hasło', models.CharField(max_length=20)),
                ('kontakt', models.CharField(blank=True, max_length=40, null=True)),
                ('data_założenia_konta', models.DateField()),
                ('czy_aktywowany', models.TextField()),
            ],
            options={
                'db_table': 'pracownicy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Punkt',
            fields=[
                ('id_punktu', models.IntegerField(primary_key=True, serialize=False)),
                ('nazwa', models.CharField(max_length=40)),
                ('kategoria', models.IntegerField()),
                ('zdjęcie', models.TextField(blank=True, null=True)),
                ('informacje', models.CharField(blank=True, max_length=50, null=True)),
                ('nr_telefonu', models.CharField(blank=True, max_length=9, null=True)),
                ('długość_geograficzna', models.FloatField()),
                ('szerokość_geograficzna', models.FloatField()),
            ],
            options={
                'db_table': 'punkt',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PunktPracownicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'punkt_pracownicy',
                'managed': False,
            },
        ),
    ]