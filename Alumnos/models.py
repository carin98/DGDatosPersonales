# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class DatosPersonales (models.Model):
    Num_cont = models.CharField(max_length=20, primary_key=True)
    Nombre = models.CharField(max_length=50)
    SEXOS = (('F', 'Femenino'), ('M', 'Masculino'))
    Sexo = models.CharField(max_length=1, choices=SEXOS, default='M')
    Edad = models.IntegerField()
    FechaNacimiento = models.DateField()
    Telefono = models.CharField(max_length=12)
    email = models.EmailField()
    Domicilio = models.TextField()

    def NombreCompleto(self):
        cadena = "{0} --> {1}"
        return cadena.format(self.Nombre, self.Edad)

    def __str__(self):
        return self.NombreCompleto()
