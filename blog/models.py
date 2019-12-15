from django.db import models
from django.utils import timezone
import secrets

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    slug = models.SlugField(unique=True, default=secrets.token_hex(15))
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    edited_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        'blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    slug = models.SlugField(unique=True, default=secrets.token_hex(15))
    created_date = models.DateTimeField(default=timezone.now)
    approve_date = models.DateTimeField(blank=True, null=True)
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.approve_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text
