from django.urls import path
from . import views

urlpatterns = [
    path('', views.greet, name='greet'),
    path('person/', views.greet_person, name='greet_person'),
]
