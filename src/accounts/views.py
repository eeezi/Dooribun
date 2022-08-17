from contextlib import redirect_stderr
from django.shortcuts import render
from django.contrib import auth

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render('home')
        else:
            return render(request, 'wrong_login.html')

    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return render('home')
