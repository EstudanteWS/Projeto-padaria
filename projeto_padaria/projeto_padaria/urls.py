from django.urls import path
from app_padaria import views

urlpatterns = [
    path('',views.home,name='home'),
    path('usuarios/',views.usuarios,name='listagem_usuarios'),
    path('listas/',views.listas,name='listas'),
    path('historia/',views.historia,name='historia'),
    path('pagamento/',views.pagamento,name='pagamento'),
    path('funcionamento/',views.funcionamento,name='funcionamento')
]
