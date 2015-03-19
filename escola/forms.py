# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import forms

__author__ = 'Administrador'

class FormTipoVida(forms.Form):
    nome = forms.CharField(max_length=30)
    situacao = forms.BooleanField()

