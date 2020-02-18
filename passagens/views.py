from django.shortcuts import render
from .forms import PassagemForms

def index(request):
        form = PassagemForms()
        contexto = {'form': form}
        return render(request, 'index.html', contexto )

def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        if form.is_valid():
            contexto = {'form': form}
            return render(request, 'revisao.html', contexto)
        else:
            print('form inválido')
            contexto = {'form': form}
            return render(request, 'index.html', contexto)