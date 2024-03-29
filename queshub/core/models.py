from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profile_pic',blank=True)
    birth_date= models.DateField(null=True, blank=True)
    about=models.TextField(max_length=150, blank=True)
    phonenumber=models.CharField(max_length=12,unique=True)

    def __str__(self):
        return self.user.username
