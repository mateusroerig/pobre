from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_expenses, name='list_expenses'),
    path('create/', views.create_expense, name='create_expense'),
    path('categories/', views.list_categories, name='list_categories'),
    path('categories/create/', views.create_category, name='create_category'),
    path('categories/editar/<int:id>/', views.edit_category, name='edit_category'),
    path('categories/excluir/<int:id>/', views.delete_category, name='delete_category'),
]
