# from datetime import date
import datetime
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=30)
    desciption = models.CharField(max_length=30)
    created_at = models.DateTimeField(models.DateTimeField(auto_now_add=True))
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
