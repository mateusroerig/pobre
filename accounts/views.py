from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Usuario
from .forms import UsuarioCreationForm

class SignUpView(CreateView):
    model = Usuario
    form_class = UsuarioCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
