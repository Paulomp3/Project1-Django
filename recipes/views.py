from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pagina3(request):
    return render(request, 'recipes/pagina3.html', context= {
        'nome': 'denise silva de carvalho vasconcelos '
    })
def pagina1(request):
    dados = 'eu sou muito lindo slk'
    context = {'chave': dados}
    return render(request, 'recipes/pagina1.html',context)
def pagina2 (request):
    return render(request,'recipes/pagina2.html', context = {
        'nome': 'paulo silva de carvalho vasconcelos'
    })

