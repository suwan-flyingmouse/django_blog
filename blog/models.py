from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # 장고의 모델을 만들면 자동으로 pk가 만들어진다.
        # 이 값을 이용해 포스트의 제목과 번호를 문자열로 표현한다.
        return f'{self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
# Create your models here.
