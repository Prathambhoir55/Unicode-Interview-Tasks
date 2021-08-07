"""UnicodeTask2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('task2home', views.task2home),
    path('task2', views.task2),
    path('task3', views.task3),
    path('pokemon', views.pokemon),
    path('allpokemon', views.allpokemon),
    path('allabilities', views.allabilities),
    path('allberries', views.allberries),
    path('task3home', views.task3home),
    path('task3bonus', views.task3bonus),
    path('pokemoninfo', views.pokemoninfo),
]
