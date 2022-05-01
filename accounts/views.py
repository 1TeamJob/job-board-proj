from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SignupForm, UserForm, ProfileForm
from django.contrib.auth import authenticate, login
from .models import Profile


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


def profile(request):
    profile = Profile.objects.get(user=request.user)    
    context = {'profile': profile}
    return render(request, 'accounts/profile.html', context)


def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.Files)
        profile_form = ProfileForm(request.POST, request.Files)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            any_profile = profile_form.save(commit=False)
            any_profile.user = request.user
            any_profile.save()
            return redirect(reverse('accounts:profile'))
    
    
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
        
    context = {}
    return render(request, 'accounts/edit_profile.html', context)



