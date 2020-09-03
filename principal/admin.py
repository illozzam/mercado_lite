from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'quantidade', 'preco']
    list_editable = ['quantidade', 'preco']
    search_fields = ['nome']
