from django import forms
from .models import User

class ProdutoForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ['cpf','nome', 'datanascimento','escola','sexo', 'peso','altura','imc','image'  ]