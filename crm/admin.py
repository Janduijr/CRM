from django.contrib import admin
from .models import Venda, Produto
# Register your models here.

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ['produto', 'quantidade', 'valor_total', 'data']

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'quantidade', 'preco']