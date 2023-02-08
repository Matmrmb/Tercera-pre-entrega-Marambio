"""Proyecto_coder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from musicos.views import (
    IndexView,
    ListarGenerosView,
    ListarInstrumentosView,
    ListarBandasView,
    AgregarGeneroView,
    AgregarInstrumentoView,
    AgregarBandaView,
    EditarGeneroView,
    EditarInstrumentoView,
    EditarBandaView,
    EliminarGeneroView,
    EliminarInstrumentoView,
    EliminarBandaView
)

app_name = 'musicos'

urlpatterns = [
    path("", include('musicos.urls', namespace='musicos')),
]