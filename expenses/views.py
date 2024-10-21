from django.shortcuts import get_object_or_404, redirect, render
from .models import Despesa, Categoria
from .forms import DespesaForm, CategoriaForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

@login_required
def create_expense(request):
    if request.method == 'POST':
        form = DespesaForm(request.POST)
        if form.is_valid():
            despesa = form.save(commit=False)
            despesa.usuario = request.user  
            despesa.save()
            form.save_m2m()  
            return redirect('list_expenses')
    else:
        form = DespesaForm()
    return render(request, 'expenses/create.html', {'form': form})

@login_required
def list_expenses(request):
    despesas = Despesa.objects.filter(usuario=request.user)

    if despesas.exists():
        valor_total = despesas.aggregate(Sum('valor'))['valor__sum'] or 0
    else:
        valor_total = 0

    return render(request, 'expenses/list.html', {
        'despesas': despesas,
        'valor_total': valor_total,
    })

@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.usuario = request.user  
            categoria.save()
            return redirect('create_expense')
    else:
        form = CategoriaForm()
    return render(request, 'expenses/categories/create.html', {'form': form})

@login_required
def list_categories(request):
    categorias = Categoria.objects.filter(usuario=request.user)
    return render(request, 'expenses/categories/list.html', {'categorias': categorias})

@login_required
def edit_category(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('list_categories')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'expenses/categories/edit.html', {'form': form})

@login_required
def delete_category(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('list_categories')
    return render(request, 'expenses/categories/delete.html', {'categoria': categoria})
