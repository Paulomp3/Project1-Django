from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pagina1(request):
    dados = 'eu sou muito lindo slk'
    context = {'chave': dados}
    return render(request, 'recipes/pagina1.html',context)


