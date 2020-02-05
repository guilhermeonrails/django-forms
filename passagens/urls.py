from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('meu_nome', views.meu_nome, name='meu_nome')
]