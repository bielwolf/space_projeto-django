from django import forms
from apps.galeria.models import Fotografia

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada']
        labels = {
            'descricao': 'Descrição da Fotografia',
            'data_fotografia': 'Data de Registro',
            'usuario': 'Usuário',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da fotografía'}),
            'legenda': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Legenda da fotografía'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição da fotografía'}),
            'data_fotografia': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control', 'type': 'date'
                }
            ),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }