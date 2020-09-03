from django.urls import path
from .views import InicialView, AdicionarProdutoView

urlpatterns = [
    path('', InicialView.as_view(), name='inicial'),
    path('adicionar-ao-carrinho/<int:produto_id>/', AdicionarProdutoView.as_view(), name='adicionar-ao-carrinho'),
]
