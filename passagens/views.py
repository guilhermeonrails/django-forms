from django.shortcuts import render, redirect
from .forms import PassagemForms

def index(request):
    form = PassagemForms()
    contexto = {'form': form}
    return render(request, 'index.html', contexto )

def meu_nome(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        if form.is_valid():
            contexto = {'form': form}
            return render(request, 'meu_nome.html', contexto)
        else:
            print('form inválido')
            form = PassagemForms()
            contexto = {'form': form}
            return render(request, 'index.html', contexto)