from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def meu_nome(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        contexto = {'nome_usado' : nome}
        return render(request, 'meu_nome.html', contexto)