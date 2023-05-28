from django.db import models
from django.utils import timezone 

# 모델을 정의 하는 코드(모델 = 객체(object))
class Post(models.Model):
    # 다른 모델에 대한 링크
    author = models.ForeignKey('auth.User')
    # 글자 수가 제한된 텍스트를 정의할 때 사용
    title = models.CharField(max_length=200)
    # 글자 수에 제한이 없는 긴 텍스트
    text = models.TextField()
    # 날짜와 시간을 의미
    created_date = models.DateTimeField(default=timezone.now)
    publisted_date = models.DateTimeField(blank = True, null = True)
    
    # 발행하는 행위(publish = 메서드의 이름)
    def publish(self):
        # 발행당시 현재 시각을 저장
        self.publisted_date = timezone.now()
        # 실제 데이터베이스에 저장
        self.save()

    def __str__(self):
        return self.title