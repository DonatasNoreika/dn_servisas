from django.db import models


# Create your models here.

class Paslauga(models.Model):
    name = models.CharField('Pavadinimas', max_length=200, help_text='Įveskite paslaugos pavadinimą')

    def __str__(self):
        return self.name

class Automobilis(models.Model):
    marke = models.CharField('Marke', max_length=200)
    modelis = models.CharField('Marke', max_length=200)

    def __str__(self):
        return f"{self.marke} {self.modelis}"


class Paslaugos_kaina(models.Model):
    paslauga_id = models.ForeignKey('Paslauga', on_delete=models.SET_NULL, null=True)
    automobiliai_ids = models.ManyToManyField(Automobilis)
    kaina = models.FloatField("Kaina")

    def __str__(self):
        return f"{self.paslauga_id.name}: {self.kaina}"


class Uzsakymas(models.Model):
    klientas = models.CharField('Klientas', max_length=200)
    automobilis_id = models.ForeignKey('Automobilis', on_delete=models.SET_NULL, null=True)
    suma = models.FloatField("Suma")

    def __str__(self):
        return f"{self.klientas}, {self.suma}"

class UzsakymoEilute(models.Model):
    paslauga_id = models.ForeignKey('Paslauga', on_delete=models.SET_NULL, null=True)
    uzsakymas_id = models.ForeignKey('Uzsakymas', related_name="Eilutės", on_delete=models.SET_NULL, null=True)
    kiekis = models.IntegerField("Kiekis", null=True)
    kaina = models.FloatField("Kaina")

    def __str__(self):
        return f"{self.paslauga_id.name}, {self.kaina}"
