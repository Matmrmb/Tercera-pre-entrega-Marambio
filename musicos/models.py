from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Instrumento(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class BandaInspiracion(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Musico(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    instrumento = models.ForeignKey(Instrumento, on_delete=models.CASCADE)
    bandas_inspiracion = models.ManyToManyField(BandaInspiracion)

    def __str__(self):
        return self.nombre