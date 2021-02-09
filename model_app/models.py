from django.db import models


# Create your models here
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)  # 게시글이 생성될 때 자동으로 현재시간이 들어감
    updated_at = models.DateTimeField(auto_now=True)

    # review_star = models.IntegerField() # 평점(별점) : 평점의 카운트를 보여주고 싶을 때, 숫자형 표현
