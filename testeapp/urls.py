
from django.urls import path, include

from . import views

#ESSE APP É FOI APENAS UM TESTE PARA TREINO - PODE SER APAGADO

urlpatterns = [
    path('testeapp', views.index)
    
]