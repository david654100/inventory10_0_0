from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            fname = form.cleaned_data.get('first_name')
            messages.success(request, f'Hello {fname}, your account is created')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        update = UserUpdateForm(request.POST, instance= request.user)

        if update.is_valid():
            update.save()
            fname = update.cleaned_data.get('first_name')
            messages.success(request, f'Hello {fname}, your account has been updated')
            return redirect('profile')
    else:
        update = UserUpdateForm(instance= request.user)
        return render(request, 'users/profile.html', {'update':update})
