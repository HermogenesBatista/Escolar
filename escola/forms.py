# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import forms
from localflavor.br.forms import BRCPFField
from escola.models import *

__author__ = 'Administrador'

class FormTipoVida(forms.Form):
    nome = forms.CharField(max_length=30)
    situacao = forms.BooleanField(required=False)


class FormResponsavel(forms.Form):

    nome = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    pai = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mae = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cpf = BRCPFField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    rg = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control'}))
    org_expedidor = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                           'pattern': '\w{3,5}\/\w{2}'}))
    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    rua = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    numero = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    bairro = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cidade = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    estado = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tel_principal = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tel_alternativo = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo_vida = forms.ChoiceField(set((c.id, c.nome) for c in TipoVida.objects.all()))
    escolaridade = forms.ChoiceField(set((x.id, x.nome) for x in Escolaridade.objects.all()))

