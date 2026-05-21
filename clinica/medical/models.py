from django.db import models
from django.contrib.auth.models import User


class Medico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuário")
    crm = models.CharField("CRM", max_length=20, unique=True)
    especialidade = models.CharField("Especialidade", max_length=100)
    telefone = models.CharField("Telefone", max_length=20, blank=True, null=True)
    bio = models.TextField("Biografia", blank=True, null=True)

    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"
        ordering = ["user__first_name"]

    def __str__(self):
        return f"Dr(a). {self.user.get_full_name() or self.user.username}"

    def get_nome(self):
        return self.user.get_full_name() or self.user.username


class Paciente(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Usuário",
        null=True,
        blank=True,
    )
    nome = models.CharField("Nome Completo", max_length=200)
    cpf = models.CharField("CPF", max_length=14, unique=True)
    data_nascimento = models.DateField("Data de Nascimento")
    telefone = models.CharField("Telefone", max_length=20)
    email = models.EmailField("E-mail", blank=True, null=True)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Consulta(models.Model):
    STATUS_CHOICES = [
        ("agendada", "Agendada"),
        ("confirmada", "Confirmada"),
        ("realizada", "Realizada"),
        ("cancelada", "Cancelada"),
    ]

    medico = models.ForeignKey(
        Medico, on_delete=models.CASCADE,
        related_name="consultas", verbose_name="Médico",
    )
    paciente = models.ForeignKey(
        Paciente, on_delete=models.CASCADE,
        related_name="consultas", verbose_name="Paciente",
    )
    data_hora = models.DateTimeField("Data e Hora")
    status = models.CharField(
        "Status", max_length=20, choices=STATUS_CHOICES, default="agendada"
    )
    observacoes = models.TextField("Observações", blank=True, null=True)
    criado_em = models.DateTimeField("Criado em", auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"
        ordering = ["-data_hora"]

    def __str__(self):
        return f"{self.paciente.nome} com {self.medico} em {self.data_hora.strftime('%d/%m/%Y %H:%M')}"

    def get_status_color(self):
        cores = {
            "agendada": "primary",
            "confirmada": "success",
            "realizada": "secondary",
            "cancelada": "danger",
        }
        return cores.get(self.status, "primary")
