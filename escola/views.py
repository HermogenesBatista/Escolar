#from django.core.serializers import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from escola.documentos import Declaracao
from escola.models import TipoEntidade
from escola.forms import FormTipoVida


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
    dados = {'name': 'Hermogenes ', 'title': 'Formulário Alunos'}
    return render(request, 'forms_aluno.html', dados)

def busca_entidade(request):

    if 'term' in request.GET:
        tags = TipoEntidade.objects.filter(
            nome__contains=request.GET['term']
        )[:10]

        #print(tags[0].nome)
        dados = json.dumps([tag.nome for tag in tags])

        print(dados)
        return HttpResponse(dados)
    return HttpResponse()

def test(request):
    if request.method == "POST":
        form = FormTipoVida(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            situacao = form.cleaned_data['situacao']

            if situacao:
                status = 'ativo'
            else:
                status = 'desativado'

            dados = {
                'nome': nome,
                'situacao': status,
                'title': 'Forms Test',
                'form': form,
                'callback': True
            }

            return render(request, 'form_teste.html', dados)

    else:

        form = FormTipoVida()

    dados = {
        'form': form,
        'title': 'Hermogenes',
        'title': 'Forms Test',
    }

    return render(request, 'form_teste.html', dados)

def declaracao(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="declaracao.pdf"'

    pdf = Declaracao(response)
    pdf.corpo()
    pdf.showPage()
    pdf.save()

    return response