from django.urls import path
from recipes.views import pagina1

urlpatterns = [

    path('', pagina1 ),
    
]