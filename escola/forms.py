# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import forms
from escola.models import *

__author__ = 'Administrador'

class FormTipoVida(forms.Form):
    nome = forms.CharField(max_length=30)
    situacao = forms.BooleanField(required=False)


class FormResponsavel(forms.Form):
    nome = forms.CharField(max_length=150)
    pai = forms.CharField(max_length=150)
    mae = forms.CharField(max_length=150)
    cpf = forms.CharField(max_length=12)
    rg = forms.CharField(max_length=25)
    org_exp = forms.CharField(max_length=10)
    dt_nasc = forms.DateField()
    rua = forms.CharField(max_length=150)
    num_rua = forms.CharField(max_length=10)
    bairro_rua = forms.CharField(max_length=30)
    cidade = forms.CharField(max_length=50)
    estado = forms.CharField(max_length=30)
    tel_principal = forms.CharField(max_length=16)
    tel_alternativo = forms.CharField(max_length=16)
    situacao = forms.BooleanField()
    tipo_vida = forms.ChoiceField(set((c.id, c.nome) for c in TipoVida.objects.all()))
    escolaridade = forms.ChoiceField(set((x.id, x.nome) for x in Escolaridade.objects.all()))

