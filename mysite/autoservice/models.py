from django.db import models


# Create your models here.

class Paslauga(models.Model):
    name = models.CharField('Pavadinimas', max_length=200, help_text='Įveskite paslaugos pavadinimą')

    def __str__(self):
        return self.name

class AutomobilioModelis(models.Model):
    marke = models.CharField('Marke', max_length=200)
    modelis = models.CharField('Marke', max_length=200)

    def __str__(self):
        return f"{self.marke} {self.modelis}"

class Automobilis(models.Model):
    klientas = models.CharField('Klientas', max_length=200, null=True)
    automobilis_id = models.ForeignKey('AutomobilioModelis', on_delete=models.SET_NULL, null=True)
    valstybinis_numeris = models.CharField('Valstybinis numeris', max_length=200, null=True)
    vin_kodas = models.CharField('VIN kodas', max_length=200, null=True)

    def __str__(self):
        return f"{self.klientas} {self.automobilis_id} {self.valstybinis_numeris} {self.vin_kodas}"


class Paslaugos_kaina(models.Model):
    paslauga_id = models.ForeignKey('Paslauga', on_delete=models.SET_NULL, null=True)
    automobiliai_ids = models.ManyToManyField(AutomobilioModelis)
    kaina = models.FloatField("Kaina")

    def display_automobiliai(self):
        return ', '.join(f"{auto.marke} {auto.modelis}" for auto in self.automobiliai_ids.all()[:3])

    display_automobiliai.short_description = 'Automobiliai'

    def __str__(self):
        return f"{self.paslauga_id.name}: {self.kaina}"


class Uzsakymas(models.Model):
    automobilis_id = models.ForeignKey('Automobilis', on_delete=models.SET_NULL, null=True)
    suma = models.FloatField("Suma")
    STATUS = (
        ('p', 'Priimtas'),
        ('v', 'Vykdomas'),
        ('a', 'Atliktas'),
        ('t', 'Atšauktas'),
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS,
        blank=True,
        default='p',
        help_text='Statusas',
    )

    def __str__(self):
        return f"{self.automobilis_id}, {self.suma}"

class UzsakymoEilute(models.Model):
    paslauga_id = models.ForeignKey('Paslauga', on_delete=models.SET_NULL, null=True)
    uzsakymas_id = models.ForeignKey('Uzsakymas', related_name="Eilutės", on_delete=models.SET_NULL, null=True)
    kiekis = models.IntegerField("Kiekis", null=True)
    kaina = models.FloatField("Kaina")

    def __str__(self):
        return f"{self.paslauga_id.name}, {self.kaina}"
