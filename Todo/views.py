from django.shortcuts import render, render_to_response,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import *
import requests


def login(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/home/')
    return render(request, 'login.html', {})


@login_required(login_url='/login/')
def index(request):
    if request.user.is_authenticated():
        response = requests.get("http://127.0.0.1:8000/api/todoitems/?format=json")
        data = [x for x in response.json()]
        return render(request, "index.html", {"data": data})

    return render(request, "login.html", {})





