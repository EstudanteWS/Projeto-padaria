from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')


def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.telefone = request.POST.get('telefone')
    novo_usuario.save()

    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request,'usuarios/usuarios.html',usuarios)

def listas(request):
    return render(request,'usuarios/listas.html')

def historia(request):
    return render(request,'usuarios/historia.html')

def pagamento(request):
    return render(request,'usuarios/pagamento.html')

def funcionamento(request):
    return render(request,'usuarios/funcionamento.html')
