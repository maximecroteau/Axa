from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.home, name='accueil'),
    path('login/', views.connexion, name='connexion'),
    path('logout', views.deconnexion, name='deconnexion'),
    path('signup', views.signup, name='signup'),
    path('home', views.home, name='home'),
]