from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

#AbstractUserクラスを継承する
class CustomUser(AbstractUser):
    pass