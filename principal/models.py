from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    def quantidade_produtos(self):
        return self.produto_set.count()

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    quantidade = models.IntegerField(default=1)
    preco = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='preço', default=0)
    no_carrinho = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['categoria', 'nome']
