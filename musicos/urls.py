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
    path('', IndexView.as_view(), name='index'),
    path('generos/', ListarGenerosView.as_view(), name='listar_generos'),
    path('instrumentos/', ListarInstrumentosView.as_view(), name='listar_instrumentos'),
    path('bandas/', ListarBandasView.as_view(), name='listar_bandas'),
    path('agregar_genero/', AgregarGeneroView.as_view(), name='agregar_genero'),
    path('agregar_instrumento/', AgregarInstrumentoView.as_view(), name='agregar_instrumento'),
    path('agregar_banda/', AgregarBandaView.as_view(), name='agregar_banda'),
    path('editar_genero/<int:pk>/', EditarGeneroView.as_view(), name='editar_genero'),
    path('editar_instrumento/<int:pk>/', EditarInstrumentoView.as_view(), name='editar_instrumento'),
    path('editar_banda/<int:pk>/', EditarBandaView.as_view(), name='editar_banda'),
    path('eliminar_genero/<int:pk>/', EliminarGeneroView.as_view(), name='eliminar_genero'),
    path('eliminar_instrumento/<int:pk>/', EliminarInstrumentoView.as_view(), name='eliminar_instrumento'),
    path('eliminar_banda/<int:pk>/', EliminarBandaView.as_view(), name='eliminar_banda'),
]