from django.contrib import admin
from .models import Categoria, Produto

class ProdutoInline(admin.TabularInline):
    model = Produto
    extra = 0

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'quantidade_produtos']
    inlines = [ProdutoInline,]

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'quantidade', 'preco']
    list_editable = ['quantidade', 'preco']
    search_fields = ['nome']
