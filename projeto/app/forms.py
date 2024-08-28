from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm):
  class Meta:
    model = Tarefa
    fields = ['titulo','prazo','responsavel','status']
    widgets = {
      'titulo': forms.TextInput(attrs={'class': 'form-control'}),
      'prazo': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
      'responsavel': forms.TextInput(attrs={'class': 'form-control'}),
    }