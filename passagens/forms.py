from django import forms
from datetime import datetime
from tempus_dominus.widgets import DatePicker
class DateInput(forms.DateInput):
    input_type = 'date'

class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100, )
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label='Ida',widget=DatePicker())
    data_volta = forms.DateField(label='Volta',widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)
    informacoes = forms.CharField(
        label='Informações extras',
        max_length=200,
        widget=forms.Textarea(),
        required=False
    )
    email = forms.EmailField(label='Email', max_length=100)

    """
    O Django fornece duas maneiras de adicionar regras de validação personalizadas a um formulário.
    clean() -> permite acessar e validar todos os campos no formulário. É executado sempre após o clean_<field>.
    clean_<field>() -> Permite definir o método de validação. Use este método se precisar lidar com várias entradas.
    """
    
    def clean_origem(self):
        origem = self.cleaned_data.get('origem')
        if any(char.isdigit() for char in origem):
            raise forms.ValidationError('Origem inválida! Não inclua números no local de origem')
        else:
            return origem
    
    def clean(self):
        origem = self.cleaned_data['origem']
        destino = self.cleaned_data['destino']
        data_pesquisa = self.cleaned_data['data_pesquisa']
        data_ida = self.cleaned_data['data_ida']
        data_volta = self.cleaned_data['data_volta']
        if origem == destino:
            self.add_error('destino','O campo destino não pode ser igual ao campo origem')
        if data_ida < data_pesquisa:
            self.add_error('data_ida','Data da ida inválida')
        if data_ida > data_volta:
            self.add_error('data_ida','Data da ida não pode ser maior que data da volta')
        return  self.cleaned_data