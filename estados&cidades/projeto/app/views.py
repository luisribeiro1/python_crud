from django.shortcuts import render
from .models import Estado
from .models import Municipio

# Criar uma função para listar os estados
def listar_estados(request):
    # Obter os dados da tabela estados no banco de dados
    lista_de_estados = Estado.objects.all()

    # Renderizar o template
    return render(request, 'app_html/lista_estados.html', {'lista_estados': lista_de_estados})


def listar_cidades(request, ufParametro):
    lista_de_municipios = Municipio.objects.filter(uf=ufParametro).order_by('municipio')

    # Formatar os valores numéricos, incluindo o separador de milhar
    for linha in lista_de_municipios:
        linha.urbana = f"{linha.urbana:,}".replace(',','.')
        linha.rural = f"{linha.rural:,}".replace(',','.')
        linha.pop2010 = f"{linha.pop2010:,}".replace(',','.')
        linha.pop2021 = f"{linha.pop2021:,}".replace(',','.')

    return render(request, 'app_html/lista_cidades.html', {'lista_municipios': lista_de_municipios})