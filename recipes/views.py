from django.shortcuts import render
from utils.recipes.factory import make_recipe

# Create your views here.
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for i in range(10)],
    })
def recipes(request):
    return render(request, 'recipes/pages/home.html',context={
        'recipes': [make_recipe() for i in range(10)]
    })
def recipes2(request, id):
    return render(request,'recipes/pages/recipe-view.html',context={
        'controle': make_recipe(),
        
    })

