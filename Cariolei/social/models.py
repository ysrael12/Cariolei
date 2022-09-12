from email.policy import default
from pyexpat import model
import uuid

from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
# Create your models here.
User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=100)
    profileimg = models.ImageField(upload_to="profile_images",default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)
    id_user = models.IntegerField()



    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(blank=True,primary_key=True, default=uuid.uuid4())
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to="post_images")
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)
    #userprofile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user