from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    is_teacher = models.BooleanField(default=False)

class Class(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class Question(models.Model):
    classs = models.ForeignKey(Class, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    question = models.TextField()




