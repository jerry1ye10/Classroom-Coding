from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signUp, name='signUp'),
    path('createUser', views.createUser, name='createUser'),
    path('auth',views.auth, name='auth'),
    path('logout', views.logOut, name='logout'),
    path('createclass',views.createClass, name='createClass'),
    path('makeclass', views.makeClass, name='makeClass'),
    path('addclass',views.addClass, name='addClass'),
    path('<int:classID>/askquestion', views.askQuestion, name ='ask'),
    path('<int:classID>/createquestion', views.createQuestion, name ='createQuestion'), 
    path('add', views.add, name ='add'), #Creates a path with the first parameter, class the function at the second parameter which that path is reached
]
