from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import FoundPetForm

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

@login_required
def report_found_pet(request):
    if request.method == 'POST':
        form = FoundPetForm(request.POST, request.FILES)
        if form.is_valid():
            found_pet = form.save(commit=False)
            found_pet.user = request.user
            found_pet.status = 'Pending'
            found_pet.save()
            return redirect('home')
    else:
        form = FoundPetForm()
    return render(request, 'report_found.html', {'form': form})
