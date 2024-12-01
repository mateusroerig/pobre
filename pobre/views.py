# views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from django.http import JsonResponse
from datetime import datetime, timedelta
import random

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"
    login_url = 'login' # URL de redirecionamento para login

def gastos_por_dia(request):
    hoje = datetime.now()
    dias = [(hoje - timedelta(days=i)).strftime('%d/%m') for i in range(7)]
    valores = [random.randint(50, 300) for _ in range(7)] # Valores simulados

    dias.reverse()
    valores.reverse()

    data = {
        "labels": dias, # Eixo X (dias) em ordem crescente
        "data": valores, # Eixo Y (valores)
    }
    return JsonResponse(data)

def categorias_de_gastos(request):
    # Simulação de dados de categorias (pode vir do banco de dados)
    categorias = ["Alimentação", "Transporte", "Saúde", "Lazer", "Educação"]
    qtdCompras = [random.randint(10, 50) for _ in categorias]
    
    data = {
        "labels": categorias, # Categorias
        "data": qtdCompras, # Quantidade de compras da categoria 
    }
    return JsonResponse(data)