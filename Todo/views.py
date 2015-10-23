from django.shortcuts import render
from django.contrib.auth import authenticate,login

from django.http import HttpResponse
import requests

def index(request):
    username = request.POST['username']
    password = request.POST['password']
    if request.user.is_authenticated():
        response = requests.get("http://127.0.0.1:8000/api/todoitems/?format=json")
        data = [x for x in response.json()]
        return render(request, "index.html", {"data": data})
    else:
        return render(request, "login.html", {})




