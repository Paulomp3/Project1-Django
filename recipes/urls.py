from django.urls import path
from recipes.views import gambiarra,raiz,pagina2

urlpatterns = [

    path('sobre/', gambiarra),
    path('', raiz ),
    path('pagina2/',pagina2)
]