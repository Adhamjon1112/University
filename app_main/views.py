from django.shortcuts import render, redirect


def home_page(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'app_main/home.html')


def teacher_page(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if not request.user.is_staff and not request.user.is_superuser:
        return redirect('home')
    

    return render(request, 'app_main/teachers.html')