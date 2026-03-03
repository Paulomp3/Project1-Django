from django.shortcuts import render


# Create your views here.
def home(request):
    dados = 'eu sou muito lindo slk'
    context = {'chave': dados}
    return render(request, 'recipes/pages/home.html',context)
def recipes(request):
    dados = 'eu sou muito lindo slk'
    context = {'chave': dados}
    return render(request, 'recipes/pages/home.html',context)
def recipes2(request, id):
    dados = 'eu sou muito lindo slk'
    context = {'chave': dados}
    return render(request,'recipes/pages/recipe-view.html',context)

