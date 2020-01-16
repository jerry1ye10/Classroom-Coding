from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
#This is where I define the models that become my database
class CustomUser(AbstractUser): #I am extending off the default abstractuser from django. The reason why I am extending is b/c django has a lot of built in functionality for it's user class and I want to keep it
    pass
    is_teacher = models.BooleanField(default=False)

class Class(models.Model): #Please note that there's no need to define primary keys in django models
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE) #use of a foreign key, don't worry about on_delete 

class Question(models.Model):
    classs = models.ForeignKey(Class, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    question = models.TextField()

class ClassStudent(models.Model):
    student =  models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    c = models.ForeignKey(Class, on_delete=models.CASCADE)
