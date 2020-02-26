from django import forms
from tempus_dominus.widgets import DatePicker
from passagens.validation import *
from passagens.models import ClasseViagem, Pessoa, Passagem
from datetime import datetime

class PassagemForm(forms.ModelForm):
    data_pesquisa = forms.DateField(disabled=True, initial=datetime.today)
    """
    Os metadados do modelo são "qualquer coisa que não seja um campo",
    como opções ordenação, nome da tabela do banco de dados (db_table)
    ou nomes no singular e no plural legíveis por humanos (verbose_name
    e verbose_name_plural)
    """
    class Meta:
        model = Passagem
        fields = ['origem', 'destino', 'data_ida', 'data_volta', 'classe_viagem','data_pesquisa', 'informacoes']
        # ou '__all__' para todos os campos
        labels = {'origem':'Origem', 'destino':'Destino', 'data_ida':'Ida', 'data_volta':'Volta', 'classe_viagem':'Classe da viagem', 'informacoes':'Informações extras'}
        widgets = {
            'data_ida':DatePicker(),
            'data_volta':DatePicker()
        }

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        lista_de_erros = {}
        campo_tem_algum_numero(origem, 'origem',lista_de_erros)
        campo_tem_algum_numero(destino, 'destino',lista_de_erros)
        origem_destino_iguais(origem, destino, lista_de_erros)
        data_ida_menor_que_data_de_hoje(data_ida, data_pesquisa, lista_de_erros)
        data_ida_maior_que_data_volta(data_ida, data_volta, lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return  self.cleaned_data

class PessoaForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        exclude = ['nome']
        labels = ['Email']
    
    def clean(self):
        pass

    # origem = forms.CharField(label='Origem', max_length=100)
    # destino = forms.CharField(label='Destino', max_length=100)
    # data_ida = forms.DateField(label='Ida',widget=DatePicker())
    # data_volta = forms.DateField(label='Volta',widget=DatePicker())
    # data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)
    # classe_viagem = forms.ChoiceField(label='Tipo de classe')
    # informacoes = forms.CharField(
    #     label='Informações extras',
    #     max_length=200,
    #     widget=forms.Textarea(),
    #     required=False
    # )
    # email = forms.EmailField(label='Email', max_length=100)

    # widget é a representação do Django de um input no HTML. 
    """
    O Django fornece duas maneiras de adicionar regras de validação personalizadas a um formulário.
    clean() -> permite acessar e validar todos os campos no formulário. É executado sempre após o clean_<field>.
    clean_<field>() -> Permite definir o método de validação. Use este método se precisar lidar com várias entradas.
    """

    # self.add_error('destino','O campo destino não pode ser igual ao campo origem')
    # self.add_error('data_ida','Data da ida não pode ser menor que a data de hoje')
    # self.add_error('data_volta','Data da volta não pode ser menor que data de ida')





