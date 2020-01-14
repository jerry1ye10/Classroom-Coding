from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from . import models

# Create your views here.
def index(request):
    '''This function renders the login page'''
    if request.user.is_authenticated:
        email = request.user.email
        return render(request, "index.html", {'user': email})
    else:
        return render(request, "login.html")

def logOut(request):
    logout(request)
    return HttpResponseRedirect("/")


def createUser(request):
    '''This function receives requests about the user's username and password from the signup form and creates users by connecting and adding to the sqlite3 database. If the registration is successful, the sign up page will redirect to the login page. Otherwise, errors will flash on the signup page.'''
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    firstName = request.POST['firstName']
    lastName = request.POST['lastName']
    user = models.CustomUser.objects.create_user(username, email, password, first_name = firstName, last_name = lastName)
    user.save()
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request,user)
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")
def signUp(request):
    return render(request, "signup.html")

def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request,user)
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")

