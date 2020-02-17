from django import forms

def origem_destino_iguais(origem, destino):
    """Verifica se origem e destino são iguais"""
    if origem == destino:
        return True

def data_ida_menor_que_data_de_hoje(data_i, data_p):
    """Verifica data de ida é menor que data a data da pesquisa"""
    if data_i < data_p:
        return True

def data_ida_maior_que_data_volta(data_i, data_v):
    """Verifica data de ida é maior que data de volta"""
    if data_i > data_v:
        return True

def campo_tem_algum_numero(campo):
        if any(char.isdigit() for char in campo):
           return True