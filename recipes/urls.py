from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.home),
    path('recipes/',views.recipes),
    path('recipes/<id>/',views.recipes2),
]