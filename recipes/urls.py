from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.home, name='recipes-home'),
    path('recipes/',views.recipes, name='recipes-list'),
    path('recipes/<id>/',views.recipes2, name='recipes-detail'),
]