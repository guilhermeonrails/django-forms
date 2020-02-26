from django import forms

def origem_destino_iguais(origem, destino, lista_de_erros):
    """Verifica se origem e destino são iguais"""
    if origem == destino:
        lista_de_erros['origem'] = 'O campo destino não pode ser igual ao campo origem'

def data_ida_menor_que_data_de_hoje(data_ida, data_pesquisa, lista_de_erros):
    """Verifica data de ida é menor que data a data da pesquisa"""
    if data_ida < data_pesquisa:
        lista_de_erros['data_ida'] = 'Data de ida não pode ser menor que a data de hoje'

def data_ida_maior_que_data_volta(data_ida, data_volta, lista_de_erros):
    """Verifica data de ida é maior que data de volta"""
    if data_ida > data_volta:
        lista_de_erros['data_volta'] = 'Data de ida não pode ser maior que a data de volta'

def campo_tem_algum_numero(valor_do_campo, nome_campo,lista_de_erros):
    """Verifica data de ida é maior que data de volta"""
    if any(char.isdigit() for char in valor_do_campo):
        lista_de_erros[nome_campo] = 'Não inclua número neste campo'

#def campo_tem_algum_numero(campo):
#    if any(char.isdigit() for char in campo):
#        return True