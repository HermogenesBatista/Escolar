from django.shortcuts import render, redirect
from django.http import HttpResponse
from escola.documentos import Declaracao

# Create your views here.
def base(request):
    #template = loader.get_template('index.html')

    return render(request, 'index.html')

def index(request):

    dados = {'name': 'Hermogenes '}
    return render(request, 'base.html', dados)

def graficos(request):

    dados = {'name': 'Hermogenes '}
    return render(request, 'charts.html', dados)

def formularios(request):

    dados = {'name': 'Hermogenes '}
    return render(request, 'forms.html', dados)

def test_redirect(request):

    return redirect(formularios)


def formulario_aluno(request):
    dados = {'name': 'Hermogenes '}
    return render(request, 'forms_aluno.html', dados)

def declaracao(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="declaracao.pdf"'

    pdf = Declaracao(response)
    pdf.corpo()
    pdf.showPage()
    pdf.save()

    return response