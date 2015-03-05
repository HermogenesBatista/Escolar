from django.shortcuts import render


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