from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

    class Meta:
        db_table = 'usuarios'

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    id_tarefa = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    prazo = models.DateField()
    responsavel = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='responsavel')
    status = models.BooleanField()

    class Meta:
        db_table = 'tarefas'
