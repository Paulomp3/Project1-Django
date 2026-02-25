from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def gambiarra(request):
    return render(request, 'recipes/gambiarra.html')
def raiz(request):
    return render(request, 'global/gambiarra2.html')
def pagina2 (request):
    return HttpResponse('pagina 2 do meu site')

