from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login
from .views import InicialView, AdicionarProdutoView

urlpatterns = [
    path('', InicialView.as_view(), name='inicial'),
    path('adicionar-ao-carrinho/<int:produto_id>/', AdicionarProdutoView.as_view(), name='adicionar-ao-carrinho'),

    path('login/', LoginView.as_view(template_name='principal/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', logout_then_login, name='logout'),
]
