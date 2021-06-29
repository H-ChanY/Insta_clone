from django.db import models

class Notice(models.Model):
    title = models.CharField(max_length=100)
    likeCount = models.IntegerField()
    viewCount = models.IntegerField()
    contents = models.TextField()

    def __str__(self):
        return f'제목:{self.title}, 좋아요수:{self.likeCount}, 조회수:{self.viewCount}'