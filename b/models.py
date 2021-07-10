from django.db import models
import random

class Blog(models.Model):
    title = models.CharField(max_length=100)
    # author : 인증 뒤에 언급을 해드리도록 하겠습니다.
    contents = models.TextField()
    r=random.randint(1,10000)
    img= models.ImageField(upload_to=f"bb/%Y/%m/%d{r}",blank=True)# blank=true는 사용자가 업로드 입력하지 않아도 된다는 의미
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    modified_at=models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return f'title:{self.title}, contents:{self.contents}'
