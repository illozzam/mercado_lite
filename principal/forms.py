from django import forms

CAMPO_NUMERO_PADRAO = forms.NumberInput(attrs={'class': 'form-control'})

class AdicionarProdutoForm(forms.Form):
    quantidade = forms.IntegerField(label='Quantidade', widget=CAMPO_NUMERO_PADRAO)
    preco = forms.DecimalField(label='Preço unitário', decimal_places=2, max_digits=5, min_value=0, widget=CAMPO_NUMERO_PADRAO)
