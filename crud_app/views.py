from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin 
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy

from .models import Cliente, Servico, Atendimento

# index view
class IndexView(TemplateView):
    template_name = "index.html"


# Creates views
class ServicoCreate(GroupRequiredMixin, LoginRequiredMixin ,CreateView):
    model = Servico
    group_required = [u'administrador', u'gerente']
    login_url = reverse_lazy('login')
    fields = [
        'nome_do_servico', 'valor', 'descricao'
    ]
    template_name = 'cadastros/form.html'
    
    def get_success_url(self):
        return reverse_lazy('listar-servico')

class ClienteCreate(GroupRequiredMixin, LoginRequiredMixin ,CreateView):
    model = Cliente
    group_required = [u'administrador', u'gerente', u'atendente']
    login_url = reverse_lazy('login')
    fields = [
        'nome_completo', 'email', 'cpf', 'data_de_nascimento', 'telefone',
        'logradouro', 'numero', 'bairro', 'cidade', 'estado'
    ]
    template_name = 'cadastros/form.html'

    def get_success_url(self):
        return reverse_lazy('listar-cliente')

class AtendimentoCreate(GroupRequiredMixin, LoginRequiredMixin ,CreateView):
    model = Atendimento
    group_required = [u'administrador', u'gerente', u'atendente']
    login_url = reverse_lazy('login')
    fields = [
        'cliente', 'servico', 'desconto', 'data_do_servico', 'situacao'
    ]
    template_name = 'cadastros/form.html'

    def form_valid(self, form):
        form.instance.registrado_por = self.request.user
        url = super().form_valid(form)
        return url

    def get_success_url(self):
        return reverse_lazy('listar-atendimento')


# Update views
class ServicoUpdate(GroupRequiredMixin, LoginRequiredMixin ,UpdateView):
    model = Servico
    group_required = [u'administrador', u'gerente']
    login_url = reverse_lazy('login')
    fields = [
        'nome_do_servico', 'valor', 'descricao'
    ]
    template_name = 'cadastros/form.html'
    
    def get_success_url(self):
        return reverse_lazy('listar-servico')

class ClienteUpdate(GroupRequiredMixin, LoginRequiredMixin ,UpdateView):
    model = Cliente
    group_required = [u'administrador', u'gerente', u'atendente']
    login_url = reverse_lazy('login')
    fields = [
        'nome_completo', 'email', 'cpf', 'data_de_nascimento', 'telefone',
        'logradouro', 'numero', 'bairro', 'cidade', 'estado'
    ]
    template_name = 'cadastros/form.html'

    def get_success_url(self):
        return reverse_lazy('listar-cliente')

class AtendimentoUpdate(GroupRequiredMixin, LoginRequiredMixin ,UpdateView):
    model = Atendimento
    group_required = [u'administrador', u'gerente', u'atendente']
    login_url = reverse_lazy('login')
    fields = [
        'cliente', 'servico', 'desconto', 'data_do_servico', 'situacao'
    ]
    template_name = 'cadastros/form.html'
    
    def get_success_url(self):
        return reverse_lazy('listar-atendimento')


# Delete views
class ServicoDelete(GroupRequiredMixin, LoginRequiredMixin ,DeleteView):
    model = Servico
    group_required = [u'administrador', u'gerente']
    login_url = reverse_lazy('login')
    template_name = 'cadastros/excluir.html'
    
    def get_success_url(self):
        return reverse_lazy('listar-servico')

class ClienteDelete(GroupRequiredMixin, LoginRequiredMixin ,DeleteView):
    model = Cliente
    group_required = [u'administrador', u'gerente']
    login_url = reverse_lazy('login')
    template_name = 'cadastros/excluir.html'

    def get_success_url(self):
        return reverse_lazy('listar-cliente')

class AtendimentoDelete(GroupRequiredMixin, LoginRequiredMixin ,DeleteView):
    model = Atendimento
    group_required = [u'administrador', u'gerente']
    login_url = reverse_lazy('login')
    template_name = 'cadastros/excluir.html'
    
    def get_success_url(self):
        return reverse_lazy('listar-atendimento')

# List views
class ServicoList(GroupRequiredMixin, LoginRequiredMixin ,ListView):
    model = Servico
    group_required = [u'administrador', u'gerente']
    login_url = reverse_lazy('login')
    fields = [
        'nome_do_servico', 'valor', 'descricao'
    ]
    template_name = 'cadastros/listas/servico.html'

    def get_queryset(self):
        self.object_list = Servico.objects.filter(registrado_por=self.request.user)
        return self.object_list

class ClienteList(GroupRequiredMixin, LoginRequiredMixin ,ListView):
    model = Cliente
    group_required = [u'administrador', u'gerente', u'atendente']
    login_url = reverse_lazy('login')
    fields = [
        'nome_completo', 'email', 'cpf', 'data_de_nascimento', 'telefone',
        'logradouro', 'numero', 'bairro', 'cidade', 'estado'
    ]
    template_name = 'cadastros/listas/cliente.html'

    def get_queryset(self):
        self.object_list = Cliente.objects.filter(registrado_por=self.request.user)
        return self.object_list

class AtendimentoList(GroupRequiredMixin, LoginRequiredMixin ,ListView):
    model = Atendimento
    group_required = [u'administrador', u'gerente', u'atendente']
    login_url = reverse_lazy('login')
    fields = [
        'cliente', 'servico', 'desconto', 'valor_total', 'data_do_servico', 'situacao'
    ]
    template_name = 'cadastros/listas/atendimento.html'

    def get_queryset(self):
        self.object_list = Atendimento.objects.filter(registrado_por=self.request.user)
        return self.object_list
