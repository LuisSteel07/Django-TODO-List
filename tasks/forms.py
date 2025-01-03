from django import forms
from django.forms import ModelForm
from .models import Tarea

class TaskForm(ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'categoria','fecha_limite', 'importante', 'public']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el Titulo'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe la Descripcion'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe la Categoria'}),
            'fecha_limite': forms.SelectDateWidget(),
            'importante': forms.CheckboxInput(),
            'public': forms.CheckboxInput(),
        }