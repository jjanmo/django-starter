from django.db import models


class Cafe(models.Model):
    name = models.CharField(max_length=20)
    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    point = models.IntegerField()
    comment = models.CharField(max_length=300)

    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)  # 카페의 정보가 삭제되면 따라서 같이 삭제 되겠다는 의미

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)