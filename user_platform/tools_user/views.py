from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomAuthenticationForm
from .forms import CustomUserCreationForm


# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the polls index.")

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente después del registro
            return redirect('home')  # Redirige a la página principal después del registro
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'login.html'
    



