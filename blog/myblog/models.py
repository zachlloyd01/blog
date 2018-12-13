from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=140)
    preview = models.CharField(max_length=300, default="Preview here!")
    body = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(default='')

    def __str__(self):
        return self.title

