from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404

from django.http import HttpResponse
from datetime import datetime

from .forms import ConnexionForm
from .forms import SignUpForm

from .models import Litige

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.


def connexion(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ConnexionForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                user = request.user
                litiges = Litige.objects.filter(fai=user)
                return render(request, 'menu/home.html', {'litiges': litiges})
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'connection/login.html', locals())

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'menu/home.html')
    else:
        form = SignUpForm()
    return render(request, 'signup/signup.html', {'form': form})

def home(request):
    user = request.user
    litiges = Litige.objects.filter(fai=user) 
    return render(request, 'menu/home.html', {'litiges': litiges})

def deconnexion(request):
    logout(request)
    return render(request, 'connection/logout.html')