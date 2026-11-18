from django.shortcuts import render
from .models import Produto
# Create your views here.

def Lista_produtos(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, 'crm/listar_produtos.html', context)