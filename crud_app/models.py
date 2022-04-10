from django.db import models
from equipe.models import Funcionario

class Cliente(models.Model):
    # dados
    nome_completo = models.CharField(max_length=60)
    email = models.EmailField()
    cpf = models.CharField(max_length=11)
    data_de_nascimento = models.DateField()
    telefone = models.CharField(max_length=11)

    # Endereço
    logradouro = models.CharField(max_length=150)
    numero = models.CharField(max_length=4)
    bairro = models.CharField(max_length=20)
    cidade = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)

    # Registro
    data_do_registro = models.DateTimeField(auto_now_add=True)
    registrado_por = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome_completo


class Servico(models.Model):
    
    # Dados do serviço
    nome_do_servico = models.CharField(max_length=60)
    valor = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    descricao = models.TextField()

    # Registro
    data_do_registro = models.DateTimeField(auto_now_add=True)
    registrado_por = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome_do_servico

class Atendimento(models.Model):
    SITUACAO_CHOICES = (
        ('Em andamento', 'Em andamento'),
        ('Concluido', 'Concluido'),
        ('Cancelado', 'Cancelado')
    )

    # Dados do atendimento
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, null=True)
    data_do_servico = models.DateTimeField() 
    situacao = models.CharField(max_length=12, choices=SITUACAO_CHOICES)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    desconto = models.DecimalField(max_digits=2, decimal_places=0, help_text='Desconto até 10%\n', null=True)
    valor_total = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, default=0)

    # Registro
    data_do_registro = models.DateTimeField(auto_now_add=True)
    registrado_por = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Atendimento #{self.id}'
    

    def save(self, *arg, **kwargs):
        self.valor_total = self.servico.valor - (self.servico.valor * (self.desconto / 100))
        self.servico.save()
        return super(Atendimento, self).save(*arg, **kwargs)
