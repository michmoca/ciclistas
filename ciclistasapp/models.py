from django.db import models
# imports

# Create your models here.
class Ciclista(models.Model):
    """docstring for Ciclista."""
    nombre = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre


class Equipo(models.Model):
    """docstring for Ciclista."""
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=50)
    nacion = models.CharField(max_length=50)
    director = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Prueba(models.Model):
    """docstring for Ciclista."""
    nombre_prueba = models.CharField(max_length=50)
    anio_edicion = models.IntegerField()
    etapas = models.IntegerField()
    total_km = models.DecimalField(max_digits=7, decimal_places=2)
    ciclista_ganador = models.ForeignKey(Ciclista)

    def __str__(self):
        return self.nombre_prueba


class CiclistaEquipo(models.Model):
    """docstring for CiclistaEquipo."""
    ciclista = models.ForeignKey(Ciclista)
    equipo = models.ForeignKey(Equipo, related_name='equipos', on_delete=models.PROTECT)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.ciclista.nombre + " - Equipo: " + self.equipo.nombre

class PruebasEquipo(models.Model):
    """docstring for PruebasEquipo."""
    equipo = models.ForeignKey(Equipo)
    prueba = models.ForeignKey(Prueba)
    puesto = models.IntegerField()

    class Meta:
        unique_together = (("equipo", "prueba"),)

    def __str__(self):
        return self.equipo.nombre + " - Prueba: " + self.prueba.nombre_prueba
