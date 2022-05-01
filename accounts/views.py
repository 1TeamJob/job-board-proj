from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/accounts/profile')
        
        
    else:
        form = SignupForm
    
    
    context = {'form': form}
    return render(request, 'registration/signup.html', context)
