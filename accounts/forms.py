from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuarioCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'nome', 'cpf', 'data_nascimento', 'cargo', 'perfil_investidor', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está em uso.")
        return email

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if Usuario.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError("Este CPF já está cadastrado.")
        return cpf

class UsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'cpf', 'data_nascimento', 'cargo', 'perfil_investidor']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está em uso.")
        return email
