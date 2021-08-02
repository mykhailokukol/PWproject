from django.shortcuts import render, redirect
from PWapp import models
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def index(request):
    lists = models.List.objects.all()
    return render(request, 'index.html', {
        'lists': lists,
    })

@login_required
def guild_lists_page(request):
    user = request.user
    try:
        userx = models.UserExtended.objects.get(user=user)
        user_guild = userx.player.guild
        lists = models.List.objects.all()
        return render(request, 'my_guild_lists.html', {
            'user_guild': user_guild,
            'lists': lists,
            'userx': userx,
        })
    except Exception:
        return redirect('/')
    return redirect('/')


def top_players_page(request):
    players_list = models.Player.objects.order_by('-CS')
    return render(request, 'top_players.html', {
        'players_list': players_list,
    })

@login_required
def create_list_page(request):
    if request.method == 'POST':
        form = CreateListForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            access = form.cleaned_data['access']
            players = form.cleaned_data['players']
            # form.creator = request.user
            form.save()
            last_list = models.List.objects.last()  #
            last_list.creator = request.user        # Я знаю, что это костыль вонючий, но, почему-то, save_model() не работает
            last_list.save()                        #
            return redirect('/')
    else:
        form = CreateListForm()
    return render(request, 'create_list.html', {
        'CreateListForm': form,
    })

def logout_page(request):
    logout(request)
    return redirect('/')

def login_page(request):
    logout(request)
    username = password = ''
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
    else:
        form = LogInForm()
    return render(request, 'auth/login.html', {
        'LogInForm': form,
    })

def sign_up_page(request):
    logout(request)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
        for field in form:
            print(field.label)
    return render(request, 'auth/sign_up.html', {
        'SignUpForm': form,
    })
