# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import reportlab
from reportlab.pdfgen import canvas

__author__ = 'Administrador'


class ReportlabCustom(canvas.Canvas):
    from reportlab.lib.pagesizes import A4
    pos_x = 0
    pos_y = A4[1]

    def set_x(self, pos_x):
        self.pos_x += pos_x

    def set_y(self, pos_y):
        self.pos_y -= pos_y

    def get_x(self):
        return self.pos_x

    def get_y(self):
        return self.pos_y

    def set_xy(self, pos_x, pos_y):
        self.pos_x += pos_x
        self.pos_y -= pos_y

    def drawCell(self, pos_x=None, pos_y=None, text='', mode=None):

        if(pos_x):
            self.set_x(pos_x)

        if(pos_y):
            self.set_y(pos_y)

        self.drawString(self.get_x(), self.get_y(), text=text, mode=mode)




class Declaracao(ReportlabCustom):

    def corpo(self):
        self.drawCell(30, 30, 'Cabeçalho')

    def getDeclaracao(self):
        '''self.header()
        self.corpo()
        self.footer()'''
        raise NotImplementedError




if __name__ == '__main__':
    pdf = ReportlabCustom('teste.pdf')
    print(pdf.get_x(), pdf.get_y())
    pdf.set_x(15)