from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=20, verbose_name='닉네임')
    email = models.EmailField(verbose_name='이메일', unique=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'my_user'

class User_Address(models.Model):
    user_addr_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    address_detail = models.CharField(max_length=100)
    request = models.TextField()

    class Meta:
        db_table = 'my_user_addr'
