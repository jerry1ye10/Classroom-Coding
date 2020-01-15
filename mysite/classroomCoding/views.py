from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from . import models

# Create your views here.
def index(request):
    '''This function renders the login page'''
    if request.user.is_authenticated:
        if request.user.is_teacher:
            classes = models.Class.objects.filter(teacher=request.user)
            classNames = []
            for c in classes:
                classNames.append(c.name)
            email = request.user.email
            return render(request, "teacherIndex.html", {'user': email, 'classes': classNames})
        else:
            email = request.user.email
            classstudents = models.ClassStudent.objects.filter(student=request.user)
            classes = []
            for clas in classstudents:
                classes.append(clas.c)
            classNames = []
            for c in classes:
                classNames.append(c.name)

            return render(request, "index.html", {'user': email, 'classes': classNames})
    else:
        return render(request, "login.html")

def addClass(request):
    if request.user.is_authenticated and request.user.is_teacher is False :
        return render(request, "addClass.html")
    else:
        return HttpResponseRedirect("/")

def add(request):
    if request.user.is_authenticated and request.user.is_teacher is False :
        className = request.POST['name']
        c = models.Class.objects.filter(name = className)[0]
        cs = models.ClassStudent(student=request.user,c=c)
        cs.save()
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")

def logOut(request):
    logout(request)
    return HttpResponseRedirect("/")

def createClass(request):
    if request.user.is_authenticated and request.user.is_teacher:
        return render(request, "createClass.html")
    else:
        return HttpResponseRedirect("/")

def makeClass(request):
    if request.user.is_authenticated and request.user.is_teacher:
        name = request.POST['name']
        u = request.user
        c = models.Class(name=name, teacher=u)
        c.save()
        return HttpResponseRedirect("/")
    else:
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

