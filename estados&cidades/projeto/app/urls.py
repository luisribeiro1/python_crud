from django.urls import path
from .views import listar_estados, listar_cidades

urlpatterns = [
    path('', listar_estados, name='listar_estados'),
    path('municipios/<str:ufParametro>/', listar_cidades, name='rotaCidades'),
]