from django.contrib.auth.models import AbstractUser
from django.db import models




# class User(AbstractUser):
#     pass

class Avatar(models.Model):
    user = models.ForeignKey(User, related_name='avatars', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img')
    created_at = models.DateTimeField(auto_now_add=True)


