from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView

from .forms import UserForm
User = get_user_model()


def user_registration(request):

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():

            if request.POST.get('password1') == request.POST.get('password2'):
                user = form.save(commit=False)
                user.set_password(request.POST.get('password1'))
                user.save()
                return redirect('login')



    form = UserForm()
    context = {
        'form': form
    }
    return render(request, 'app_users/registration.html', context)


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user_exists = user.check_password(password)
        except:
            user_exists = None
            user = None

        if user_exists:
            login(request, user)
            return redirect('home')
    return render(request, 'app_users/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')
