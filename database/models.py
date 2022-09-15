from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,max_length=250,default=None)
#    id_user = models.IntegerField()
#    password = models.CharField(max_length=250)
    name = models.CharField(max_length=250,default=None)
    email = models.EmailField(null=True)
    bio = models.CharField(max_length=100,null=True)
    profile_pic = models.ImageField(upload_to="profile_pics",null=True,default="profiles/myimages/empty_images.jpg")

    def __str__(self):
        return self.user.username


class Profile_pic(models.Model):
    pass
