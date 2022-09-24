from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todolist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(datetime.now, default=datetime.now)
    title = models.CharField(max_length=300)
    description = models.TextField()
