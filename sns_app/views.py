from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def signup(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']

        try:
            User.objects.get(username=username2)
            return render(request, 'signup.html', {'error': 'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(username2, '', password2)
            return render(request, 'signup.htl', {})

    return render(request, 'signup.html', {})


def loginfnc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)

        if user is not None:
            login(request, user)
            return render('list')
        else:
            return redirect()
    else:
        return render(request, 'login.html')
