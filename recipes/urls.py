from django.urls import path
from recipes.views import pagina3,pagina1,pagina2 

urlpatterns = [

    path('pagina3/', pagina3),
    path('', pagina1 ),
    path('pagina2/',pagina2)
]