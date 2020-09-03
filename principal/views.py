from django.shortcuts import render, redirect
from django.views import View
from .models import Categoria, Produto
from .forms import AdicionarProdutoForm

class InicialView(View):
    dados = {}
    template = ''

    def get(self, request, **kwargs):
        self.template = 'principal/base.html'

        self.dados['valor_total'] = 0
        for produto in Produto.objects.all():
            self.dados['valor_total'] += produto.quantidade * produto.preco

        self.dados['categorias_compras'] = Categoria.objects.all()
        return render(request, self.template, self.dados)

class AdicionarProdutoView(View):
    dados = {}
    template = 'principal/adicionar-ao-carrinho.html'

    def get(self, request, **kwargs):
        self.dados['produto'] = Produto.objects.get(id=self.kwargs['produto_id'])

        formulario_inicial = {
            'quantidade': self.dados['produto'].quantidade,
        }

        self.dados['formulario'] = AdicionarProdutoForm(initial=formulario_inicial)
        return render(request, self.template, self.dados)

    def post(self, request, **kwargs):
        self.dados['produto'] = Produto.objects.get(id=self.kwargs['produto_id'])
        self.dados['formulario'] = AdicionarProdutoForm(request.POST)
        if self.dados['formulario'].is_valid():
            self.dados['produto'].quantidade = self.dados['formulario'].cleaned_data['quantidade']
            self.dados['produto'].preco = self.dados['formulario'].cleaned_data['preco']
            self.dados['produto'].save()
            return redirect('principal:inicial')
        else:
            return render(request, self.template, self.dados)
