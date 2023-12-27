from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(verbose_name = 'Имя пользователя', max_length = 50)
    email = models.EmailField(unique = True, verbose_name = 'почта')
    name = models.CharField(null = False, blank = False, verbose_name = 'имя') 
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []