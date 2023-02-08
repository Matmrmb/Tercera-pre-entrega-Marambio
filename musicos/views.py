from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Musico, Genero, Instrumento, BandaInspiracion
from .forms import MusicoForm, GeneroForm, InstrumentoForm, BandaInspiracionForm

class IndexView(ListView):
    template_name = 'musicos/index.html'
    context_object_name = 'musicos'
    model = Musico
    

class ListarGenerosView(ListView):
    template_name = 'musicos/listar_generos.html'
    context_object_name = 'generos'
    model = Genero

class ListarInstrumentosView(ListView):
    template_name = 'musicos/listar_instrumentos.html'
    context_object_name = 'instrumentos'
    model = Instrumento

class ListarBandasView(ListView):
    template_name = 'musicos/listar_bandas.html'
    context_object_name = 'bandas'
    model = BandaInspiracion

class AgregarGeneroView(CreateView):
    template_name = 'musicos/agregar_genero.html'
    form_class = GeneroForm
    success_url = reverse_lazy('musicos:listar_generos')

class AgregarInstrumentoView(CreateView):
    template_name = 'musicos/agregar_instrumento.html'
    form_class = InstrumentoForm
    success_url = reverse_lazy('musicos:listar_instrumentos')

class AgregarBandaView(CreateView):
    template_name = 'musicos/agregar_banda.html'
    form_class = BandaInspiracionForm
    success_url = reverse_lazy('musicos:listar_bandas')

class EditarGeneroView(UpdateView):
    template_name = 'musicos/editar_genero.html'
    form_class = GeneroForm
    model = Genero
    success_url = reverse_lazy('musicos:listar_generos')

class EditarInstrumentoView(UpdateView):
    template_name = 'musicos/editar_instrumento.html'
    form_class = InstrumentoForm
    model = Instrumento
    success_url = reverse_lazy('musicos:listar_instrumentos')

class EditarBandaView(UpdateView):
    template_name = 'musicos/editar_banda.html'
    form_class = BandaInspiracionForm
    model = BandaInspiracion
    success_url = reverse_lazy('musicos:listar_bandas')

class EliminarGeneroView(DeleteView):
    template_name = 'musicos/eliminar_genero.html'
    model = Genero
    success_url = reverse_lazy('musicos:listar_generos')

class EliminarInstrumentoView(DeleteView):
    template_name = 'musicos/eliminar_instrumento.html'
    model = Instrumento
    success_url = reverse_lazy('musicos:listar_instrumentos')

class EliminarBandaView(DeleteView):
    template_name = 'musicos/eliminar_banda.html'
    model = BandaInspiracion
    success_url = reverse_lazy('musicos:listar_bandas')

