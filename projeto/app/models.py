from django.db import models

# Create your models here.
class Tarefa(models.Model):
    id_tarefa = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    prazo = models.DateField()
    responsavel = models.CharField(max_length=100)
    status = models.BooleanField()

    class Meta:
        db_table = 'tarefas'

