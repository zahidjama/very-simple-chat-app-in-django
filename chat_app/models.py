from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import CustomUserManager
# Create your models here.



class CustomUser(AbstractBaseUser):
    email=models.EmailField(verbose_name="Email Address", unique=True)
    name=models.CharField(verbose_name="Full Name", max_length=123)
    phone=models.IntegerField(verbose_name="Phone Number")

    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    object=CustomUserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name', 'phone']


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Message(models.Model):
    msg=models.TextField()
    sender=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)