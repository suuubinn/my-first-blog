from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    # 전체 글 목록을 가져옴
    qs = Post.objects.all()
    # 발행날짜가 현재와 같거나 작은 것만 가지고옴
    qs = qs.filter(publisted_date__lte=timezone.now())
    qs = qs.order_by('publisted_date')
    # render은 장고가 지원해주는 템플릿 시스템
    return render(request, 'blog/post_list.html', {
        'post_list': qs,
    })

def post_detail(request):
    return render(request, 'blog/post_detail.html')