from django.shortcuts import render
from passagens.forms import PassagemForm, PessoaForms 
from django.forms import modelform_factory

def index(request):
    form =  PassagemForm()
    pessoa_form = PessoaForms()
    contexto = {'form': form, 'pessoa_form':pessoa_form}
    return render(request, 'index.html', contexto )

def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagemForm(request.POST)
        pessoa_form = PessoaForms(request.POST)
        if form.is_valid():
            contexto = {'form': form, 'pessoa_form':pessoa_form}
            return render(request, 'revisao.html', contexto)
        else:
            print('form inválido')
            contexto = {'form': form}
            return render(request, 'index.html', contexto)