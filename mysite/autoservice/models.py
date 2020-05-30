from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Paslauga(models.Model):
    name = models.CharField('Pavadinimas', max_length=200, help_text='Įveskite paslaugos pavadinimą')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Paslauga'
        verbose_name_plural = 'Paslaugos'

class AutomobilioModelis(models.Model):
    marke = models.CharField('Marke', max_length=200)
    modelis = models.CharField('Marke', max_length=200)

    def __str__(self):
        return f"{self.marke} {self.modelis}"

    class Meta:
        verbose_name = 'Automobilio modelis'
        verbose_name_plural = 'Automobilio modeliai'

class Automobilis(models.Model):
    klientas = models.CharField('Klientas', max_length=200, null=True)
    automobilis_id = models.ForeignKey('AutomobilioModelis', on_delete=models.SET_NULL, null=True)
    valstybinis_numeris = models.CharField('Valstybinis numeris', max_length=200, null=True)
    vin_kodas = models.CharField('VIN kodas', max_length=200, null=True)

    def __str__(self):
        return f"{self.klientas} {self.automobilis_id} {self.valstybinis_numeris} {self.vin_kodas}"

    class Meta:
        verbose_name = 'Automobilis'
        verbose_name_plural = 'Automobiliai'


class Paslaugos_kaina(models.Model):
    paslauga_id = models.ForeignKey('Paslauga', on_delete=models.SET_NULL, null=True)
    automobiliai_ids = models.ManyToManyField(AutomobilioModelis)
    kaina = models.FloatField("Kaina")

    def display_automobiliai(self):
        return ', '.join(f"{auto.marke} {auto.modelis}" for auto in self.automobiliai_ids.all()[:3])

    display_automobiliai.short_description = 'Automobiliai'

    def __str__(self):
        return f"{self.paslauga_id.name}: {self.kaina}"

    class Meta:
        verbose_name = 'Paslaugų kaina'
        verbose_name_plural = 'Paslaugų kainos'


class Uzsakymas(models.Model):
    automobilis_id = models.ForeignKey('Automobilis', on_delete=models.SET_NULL, null=True)
    klientas_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    grazinimo_laikas = models.DateTimeField('Gražinimo terminas', null=True, blank=True)
    # suma = models.FloatField("Suma")
    STATUS = (
        ('p', 'Priimtas'),
        ('v', 'Vykdomas'),
        ('a', 'Atliktas'),
        ('t', 'Atšauktas'),
    )

    @property
    def suma(self):
        eilutes = UzsakymoEilute.objects.filter(uzsakymas_id=self.pk)
        suma = 0
        for eilute in eilutes:
            eilutes_suma = eilute.kiekis * eilute.kaina
            suma += eilutes_suma
        return suma

    @property
    def pasibaige_terminas(self):
        if self.grazinimo_laikas and datetime.today() > self.grazinimo_laikas:
            return True
        return False

    status = models.CharField(
        max_length=1,
        choices=STATUS,
        blank=True,
        default='p',
        help_text='Statusas',
    )

    def __str__(self):
        return f"{self.automobilis_id}, {self.suma}"

    class Meta:
        verbose_name = 'Užsakymas'
        verbose_name_plural = 'Užsakymai'

class UzsakymoEilute(models.Model):
    paslauga_id = models.ForeignKey('Paslauga', on_delete=models.SET_NULL, null=True)
    uzsakymas_id = models.ForeignKey('Uzsakymas', related_name="eilutes", on_delete=models.SET_NULL, null=True)
    kiekis = models.IntegerField("Kiekis", null=True)
    kaina = models.FloatField("Kaina")

    @property
    def suma(self):
        return self.kiekis * self.kaina

    def __str__(self):
        return f"{self.paslauga_id.name}, {self.kaina}"

    class Meta:
        verbose_name = 'Užsakymo eilutė'
        verbose_name_plural = 'Užsakymo eilutės'
