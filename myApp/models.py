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
    profile_pic = models.ImageField(upload_to='Media/profile_pic', null= True )

    def __str__(self) -> str:
        return self.username


class viewersProfileModel(models.Model):
    
    PREFERRED_CONTENT=[
        ('articles', 'Articles'),
        ('videos', 'Videos'),
        ('podcasts', 'Both'),
    ]

    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='viewersProfile')
    Bio=models.TextField(max_length=100,null=True)
    interests = models.CharField(max_length=255, blank=True, null=True) 
    preferred_content_type = models.CharField(max_length=100, choices=PREFERRED_CONTENT, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}"   
    
class BloggerProfileModel(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,related_name='bloggersProfile')
    Bio = models.TextField(blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}"      