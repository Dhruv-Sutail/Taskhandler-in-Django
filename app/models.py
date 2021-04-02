from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TODO(models.Model):
    status_choices = [
        ('Completed','Completed'),
        ('Pending','Pending')
    ]
    priority_choices = [
        ('High','High'),
        ('Medium','Medium'),
        ('Low','Low')
    ]
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=10 , choices = status_choices)
    date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=10 , choices = priority_choices)
    user = models.ForeignKey(User , on_delete = models.CASCADE)
