from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bem-vindo ao Marketplace de Vídeos e Produtos Físicos!")

