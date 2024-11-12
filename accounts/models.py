from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    INVESTIDOR_CHOICES = [
        ('Passivo', 'Passivo'),
        ('Agressivo', 'Agressivo'),
    ]

    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    cargo = models.CharField(max_length=100)
    perfil_investidor = models.CharField(max_length=100, choices=INVESTIDOR_CHOICES)
