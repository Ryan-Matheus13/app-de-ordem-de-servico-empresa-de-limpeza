from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Atendimento, Cliente, Servico
from crud_app.forms import descontoForm

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome_do_servico", "valor", "descricao", "data_do_registro")
    list_display_links = ("nome_do_servico",)
    fieldsets = (
        ('Dados do serviços', {
            'classes': ('extrapretty'),
            'fields': ('nome_do_servico', 'valor', 'descricao')
        }),
    )

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("id", "nome_completo", "email", "cpf", "data_do_registro")
    list_display_links = ("nome_completo",)
    fieldsets = (
        ('Dados', {
            'classes': ('extrapretty'),
            'fields': ('nome_completo', 'email', 'cpf', 'data_de_nascimento', 'telefone')
        }),
        ('Endereço', {
            'classes': ('extrapretty'),
            'fields': ('logradouro', 'numero', 'bairro', 'cidade', 'estado')
        })
    )


@admin.register(Atendimento)
class AtendimentoAdmin(ImportExportModelAdmin):
    readonly_fields = ("valor_final",)
    list_display = ("id", "cliente", "servico", "valor_final", "situacao","data_do_servico", "registrado_por")
    list_display_links = ("cliente",)
    raw_id_fields = ['cliente']
    ordering = ('data_do_registro',)
    list_filter = ('data_do_registro',)
    form = descontoForm
    fieldsets = (
        ('Dados do atendimento', {
            'classes': ('extrapretty'),
            'fields': ('cliente', 'servico', 'desconto', 'valor_final', 'data_do_servico', 'situacao')
        }),
    )
    def valor_final(self, obj: Atendimento) -> str:
        return f'R$ {(obj.valor_total)}'

    # Função que captura o usuário logado
    def save_model(self, request, obj, form, change):
        usuario = request.user
        obj.registrado_por = usuario
        super(AtendimentoAdmin, self).save_model(request, obj, form, change)

