from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Paciente


class RegistroForm(UserCreationForm):
    nome = forms.CharField(label="Nome Completo", max_length=200)
    cpf = forms.CharField(label="CPF", max_length=14)
    data_nascimento = forms.DateField(
        label="Data de Nascimento",
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    telefone = forms.CharField(label="Telefone", max_length=20)
    email = forms.EmailField(label="E-mail", required=False)

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get("email", "")
        if commit:
            user.save()
            Paciente.objects.create(
                user=user,
                nome=self.cleaned_data["nome"],
                cpf=self.cleaned_data["cpf"],
                data_nascimento=self.cleaned_data["data_nascimento"],
                telefone=self.cleaned_data["telefone"],
                email=self.cleaned_data.get("email"),
            )
        return user
