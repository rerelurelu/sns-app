from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from . import models


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
            return redirect('list')
        else:
            return redirect('login')
    return render(request, 'login.html')


@login_required
def listfnc(request):
    object_list = models.SnsModel.objects.all()
    return render(request, 'list.html', {'object_list': object_list})


def logoutfnc(request):
    logout(request)
    return redirect('login')


def detailfnc(request, pk):
    objects = models.SnsModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object': objects})


def goodfnc(request, pk):
    post = models.SnsModel.objects.get(pk=pk)
    post.good += 1
    post.save()
    return redirect('list')


def readfnc(request, pk):
    post = models.SnsModel.objects.get(pk=pk)
    post2 = request.user.get_username()

    if post2 in post.read_text:
        return redirect('list')
    else:
        post.read += 1
        post.read_text = post.read_text + ' ' + post2
        post.save()
        return redirect('list')


class SnsCreate(generic.CreateView):
    template_name = 'create.html'
    model = models.SnsModel
    fields = ('title', 'contents', 'author', 'images')
    success_url = reverse_lazy('list')
