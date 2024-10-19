from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser (AbstractUser):

    USER = [
        ('blogger','Blogger'),
        ('viewer','Viewer'),
    ]

    GENDER = [
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ]

    usertype = models.CharField(choices= USER, max_length= 100, null= True )
    gender = models.CharField(choices= GENDER, max_length= 100, null= True )
    age = models.PositiveIntegerField(null= True )
    contact_no = models.CharField(max_length= 100, null= True )

    def __str__(self) -> str:
        return self.username
