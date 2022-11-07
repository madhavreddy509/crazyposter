from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
class Post(models.Model):
    title=models.CharField( max_length=100)
    content=models.TextField()
    photo=models.ImageField(default='default.jpg',upload_to='blog_pictures', height_field=None, width_field=None, max_length=None)
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
    
