from django.shortcuts import render


# Create your views here.
def home(request):
    dados = 'eu sou muito lindo slk'
    context = {'chave': dados}
    return render(request, 'recipes/home.html',context)


