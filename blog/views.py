from django.shortcuts import render
from .models import Post # models.py에 정의된 Post 모델 import

def index(request):
    posts = Post.objects.all().order_by('-pk') # 모든 Post 레코드를 가져와 posts에 저장하는 쿼리

    return render( #render : 장고가 기본적으로 제공하는 함수.
        request,
        'blog/index.html',
        {
            'posts': posts, # render 함수 안에 posts를 딕셔너리 형태로 추가
        }
    )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk) # pk를 매개변수로 받아 일치하는 pk의 Post 레코드를 호출

    return render(
        request,
        'blog/single_post_page.html', # post 한 개를 sing~.html에 렌더링
        {
            'post' : post,
        }
    )
