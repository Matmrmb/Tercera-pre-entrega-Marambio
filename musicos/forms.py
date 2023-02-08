from django import forms
from .models import Musico, Genero, Instrumento, BandaInspiracion

class MusicoForm(forms.ModelForm):
    class Meta:
        model = Musico
        fields = ['nombre', 'genero', 'instrumento', 'bandas_inspiracion']

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nombre']

class InstrumentoForm(forms.ModelForm):
    class Meta:
        model = Instrumento
        fields = ['nombre']

class BandaInspiracionForm(forms.ModelForm):
    class Meta:
        model = BandaInspiracion
        fields = ['nombre']