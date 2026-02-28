from django.shortcuts import render


# Create your views here.
def home(request):
    dados = 'eu sou muito lindo slk'
    context = {'chave': dados}
    return render(request, 'recipes/pages/home.html',context)


