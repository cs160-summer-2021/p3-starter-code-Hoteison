from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.index, name='demo'),
    path('new_interaction', views.new_interaction, name='new_interaction'),
    path('start_screen', views.start_screen, name='start_screen'),
    path('animals', views.animals, name='animals'),
    path('flowers', views.flowers, name='flowers'),
    path('landscapes', views.landscapes, name='landscapes')
]
