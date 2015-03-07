# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from reportlab.pdfgen import canvas

__author__ = 'Administrador'

class Declaracao(canvas.Canvas):

    def corpo(self):
        self.drawString(10, 600, 'Oiiiiiiiiii')