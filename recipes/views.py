from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def gambiarra(request):
    return render(request, 'gambiarra.html')
def raiz(request):
    return HttpResponse('raiz do meu lindo site')
def pagina2 (request):
    return HttpResponse('pagina 2 do meu site')

