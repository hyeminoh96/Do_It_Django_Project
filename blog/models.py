from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%M/%d/', blank=True) # 이미지를 저장할 폴더의 경로 규칙
    # note.하위 폴더를 깊게 지정해야 탐색 시간 단축
    # note. blank=True : 해당 필드가 필수 항목은 아님
    file_upload = models.FileField(upload_to='blog/files/%Y/%M/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # author 필드 추가
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) # 작성자가 db에서 삭제되어도 포스트를 삭제하지 않고 작성자명을 빈칸으로 둠

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}' # pk field에 포스트의 제목과 번호를 문자열로 표현

    def get_absolute_url(self): # 모델의 레코드별 url 생성 규칙
        return f'/blog/{self.pk}/' # blog 뒤에 post의 pk를 붙임
