from django.db import models

class Notice(models.Model):
    title = models.CharField(max_length=100)
    likeCount = models.IntegerField()
    viewCount = models.IntegerField()
    contents = models.TextField()

    def __str__(self):
        return f'{self.title} !!! {self.likeCount}'