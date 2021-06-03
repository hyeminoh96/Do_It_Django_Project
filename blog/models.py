from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # author : 추후 작성 예정


    def __str__(self):
        return f'[{self.pk}]{self.title}' # pk field에 포스트의 제목과 번호를 문자열로 표현

