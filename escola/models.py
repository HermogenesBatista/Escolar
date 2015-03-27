from django.db import models

# Create your models here.
class Turma(models.Model):
    nome = models.CharField(max_length=30)
    situacao = models.BooleanField(default=True)

class Escolaridade(models.Model):
    nome = models.CharField(max_length=30)
    situacao = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class TipoVida(models.Model):
    nome = models.CharField(max_length=30)
    situacao = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class TipoEntidade(models.Model):
    nome = models.CharField(max_length=100)
    situacao = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Permissoes(models.Model):
    nome = models.CharField(max_length=30)
    situacao = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Perfil(models.Model):
    nome = models.CharField(max_length=30)
    permissao = models.ManyToManyField(Permissoes)
    situacao = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    nome = models.CharField(max_length=150)
    pai = models.CharField(max_length=150)
    mae = models.CharField(max_length=150)
    cpf = models.CharField(max_length=12)
    rg = models.CharField(max_length=25)
    org_exp = models.CharField(max_length=10)
    dt_nasc = models.DateField()
    rua = models.CharField(max_length=150)
    num_rua = models.CharField(max_length=10)
    bairro_rua = models.CharField(max_length=30)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=30)
    tel_principal = models.CharField(max_length=16)
    tel_alternativo = models.CharField(max_length=16)
    situacao = models.BooleanField(default=True)
    tipo_vida = models.ForeignKey(TipoVida)

    class Meta:
        abstract = True

class Responsavel(Pessoa):
    escolaridade = models.ForeignKey(Escolaridade)

    def __str__(self):
        return self.nome


class Entidade(models.Model):
    nome = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=15)
    rua = models.CharField(max_length=150)
    num_rua = models.CharField(max_length=10)
    bairro_rua = models.CharField(max_length=30)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=30)
    codInep = models.IntegerField(max_length=10)
    tel_principal = models.CharField(max_length=16)
    tel_alternativo = models.CharField(max_length=16)
    tipo_entidade = models.ForeignKey(TipoEntidade)
    responsavel = models.ManyToManyField(Responsavel)
    situacao = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Aluno(Pessoa):
    escola = models.ForeignKey(Entidade, default=1)
    ano_ensino = models.ForeignKey(Turma)

    def __str__(self):
        return self.nome