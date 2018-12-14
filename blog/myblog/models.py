from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=140)
    preview = models.CharField(max_length=300, default="")
    body = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to = "myblog/img")

    def __str__(self):
        return self.title

