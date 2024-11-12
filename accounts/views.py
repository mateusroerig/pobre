from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .models import Usuario
from .forms import UsuarioCreationForm, UsuarioUpdateForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class SignUpView(CreateView):
    model = Usuario
    form_class = UsuarioCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

@method_decorator(login_required, name='dispatch')
class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioUpdateForm
    template_name = 'registration/update_user_info.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user
