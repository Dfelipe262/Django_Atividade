from django.shortcuts import render, get_object_or_404
from .models import Postagem_Alimentos, Postagem_Apicultura, Postagem_Informatica

def pagina_inicial(request):
    return render(request,'pagina_inicial.html')


def pagina_informatica(request):
    postagem = Postagem_Informatica.objects.all()
    context={
        'objeto' : postagem, 
    }
    return render(request,'pagina_informatica.html',context) 



def pagina_apicultura(request):
    postagem = Postagem_Apicultura.objects.all()
    context={
        'objeto' : postagem, 
    }
    return render(request,'pagina_apicultura.html',context) 



def pagina_alimentos(request):
    postagem = Postagem_Alimentos.objects.all()
    context={
        'objeto' : postagem, 
    }
    return render(request,'pagina_alimentos.html',context) 




