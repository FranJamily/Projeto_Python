from django.shortcuts import render


def index(request):
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')

def base(request):
    return render(request, 'galeria/base.html')
# Create your views here.
