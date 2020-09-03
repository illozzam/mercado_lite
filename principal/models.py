from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    quantidade = models.IntegerField(default=1)
    preco = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='preço', default=0)
    no_carrinho = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
