from django.db import models

# Criação do modelo Estado
class Estado(models.Model):
    uf = models.CharField(max_length=2, primary_key=True)
    estado = models.CharField(max_length=100)
    cidades = models.IntegerField()
    capital = models.CharField(max_length=100)
    gentilico = models.CharField(max_length=100)

    # Informar que a tabela já existe e não deve ser criada
    class Meta:
        db_table = 'estados'


class Municipio(models.Model):
    codigo = models.IntegerField(primary_key=True)
    uf = models.CharField(max_length=2)
    municipio = models.CharField(max_length=100)
    urbana = models.FloatField()
    rural = models.FloatField()
    pop2010 = models.IntegerField()
    pop2021 = models.IntegerField()

    class Meta:
        db_table = 'cidades'