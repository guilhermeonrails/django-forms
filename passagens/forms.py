from django import forms
from datetime import datetime
from tempus_dominus.widgets import DatePicker
from passagens.validation import *
from passagens.classe_viagem import tipos_de_classes

class PassagemForms(forms.Form):
    #4 primeiros passagem, 
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label='Ida',widget=DatePicker())
    data_volta = forms.DateField(label='Volta',widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)
    classe_viagem = forms.ChoiceField(label='Tipo de classe',choices=tipos_de_classes)
    informacoes = forms.CharField(
        label='Informações extras',
        max_length=200,
        widget=forms.Textarea(),
        required=False
    )
    email = forms.EmailField(label='Email', max_length=100)

    # widget é a representação do Django de um input no HTML. 
    """
    O Django fornece duas maneiras de adicionar regras de validação personalizadas a um formulário.
    clean() -> permite acessar e validar todos os campos no formulário. É executado sempre após o clean_<field>.
    clean_<field>() -> Permite definir o método de validação. Use este método se precisar lidar com várias entradas.
    """

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        lista_de_erros = {}
        origem_destino_iguais(origem, destino, lista_de_erros)
        data_ida_menor_que_data_de_hoje(data_ida, data_pesquisa, lista_de_erros)
        data_ida_maior_que_data_volta(data_ida, data_volta, lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return  self.cleaned_data

    # self.add_error('destino','O campo destino não pode ser igual ao campo origem')
    # self.add_error('data_ida','Data da ida não pode ser menor que a data de hoje')
    # self.add_error('data_volta','Data da volta não pode ser menor que data de ida')





