# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import DatosPersonales

# Create your views here.
def index(request):

    return render(request, 'Alumnos/index.html', )

def res(request):
    Datos = DatosPersonales.objects.all()
    return render(request, 'Alumnos/resultado.html', {"Alumnos":Datos})