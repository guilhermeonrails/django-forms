from django import forms
from datetime import datetime

class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100, )
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label='Ida', )
    data_volta = forms.DateField(label='Volta')
    data_pesquisa = forms.DateField(disabled=True,initial=datetime.today)
    informacoes = forms.CharField(
        label='Informações extras',
        max_length=200,
        widget=forms.Textarea()
    )
    email = forms.EmailField(label='Email', max_length=100)
    
