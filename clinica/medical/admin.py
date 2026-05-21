from django.contrib import admin
from django.utils.html import format_html
from .models import Medico, Paciente, Consulta


class ConsultaInlinePaciente(admin.TabularInline):
    model = Consulta
    extra = 0
    fields = ("medico", "data_hora", "status", "observacoes")
    show_change_link = True
    verbose_name = "Consulta"
    verbose_name_plural = "Consultas do Paciente"


class ConsultaInlineMedico(admin.TabularInline):
    model = Consulta
    extra = 0
    fields = ("paciente", "data_hora", "status")
    show_change_link = True
    verbose_name = "Consulta"
    verbose_name_plural = "Consultas do Médico"


@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ("get_nome_display", "crm", "especialidade", "telefone", "total_consultas")
    list_filter = ("especialidade",)
    search_fields = ("user__username", "user__first_name", "user__last_name", "crm", "especialidade")
    inlines = [ConsultaInlineMedico]
    fieldsets = (
        ("Dados Pessoais", {"fields": ("user", "crm", "telefone")}),
        ("Especialização", {"fields": ("especialidade", "bio")}),
    )

    @admin.display(description="Nome")
    def get_nome_display(self, obj):
        return str(obj)

    @admin.display(description="Consultas")
    def total_consultas(self, obj):
        return obj.consultas.count()


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "cpf", "telefone", "email", "data_nascimento", "total_consultas")
    search_fields = ("nome", "cpf", "email")
    list_filter = ("data_nascimento",)
    inlines = [ConsultaInlinePaciente]
    fieldsets = (
        ("Dados Pessoais", {"fields": ("user", "nome", "cpf", "data_nascimento")}),
        ("Contato", {"fields": ("telefone", "email")}),
    )

    @admin.display(description="Consultas")
    def total_consultas(self, obj):
        return obj.consultas.count()


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ("paciente", "medico", "data_hora", "status_badge", "criado_em")
    list_filter = ("status", "data_hora", "medico__especialidade")
    search_fields = ("paciente__nome", "paciente__cpf", "medico__user__first_name", "medico__crm")
    date_hierarchy = "data_hora"
    readonly_fields = ("criado_em",)
    fieldsets = (
        ("Agendamento", {"fields": ("paciente", "medico", "data_hora", "status")}),
        ("Detalhes", {"fields": ("observacoes", "criado_em"), "classes": ("collapse",)}),
    )

    @admin.display(description="Status")
    def status_badge(self, obj):
        cores = {
            "agendada": "#0d6efd",
            "confirmada": "#198754",
            "realizada": "#6c757d",
            "cancelada": "#dc3545",
        }
        cor = cores.get(obj.status, "#0d6efd")
        return format_html(
            '<span style="background:{};color:#fff;padding:3px 10px;border-radius:12px;font-size:12px;">{}</span>',
            cor, obj.get_status_display(),
        )
