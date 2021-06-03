from django.shortcuts import render
from django.views.generic import ListView # 장고 내장 함수 ListView를 import
from .models import Post

# !!ListView는 모델명 뒤에 '_list'가 붙은 html 파일을 기본 템플릿으로 사용!!

class PostList(ListView): # ListView 클래스를 상속하는 PostList 클래스
    model = Post
    # CBV에서 최신 포스트 순으로 보여주는 기능을 제공
    ordering = '-pk'

    # FBV로 template_name을 직접 지정하는 방식
    # template_name = 'blog/post_list.html'


###### FBV로 페이지 만들기

# from django.shortcuts import render
# from .models import Post # models.py에 정의된 Post 모델 import
#
# def index(request):
#     posts = Post.objects.all().order_by('-pk') # 모든 Post 레코드를 가져와 posts에 저장하는 쿼리
#
#     return render( #render : 장고가 기본적으로 제공하는 함수.
#         request,
#         'blog/post_list.html',
#         {
#             'posts': posts, # render 함수 안에 posts를 딕셔너리 형태로 추가
#         }
#     )
#
def single_post_page(request, pk):
    post = Post.objects.get(pk=pk) # pk를 매개변수로 받아 일치하는 pk의 Post 레코드를 호출

    return render(
        request,
        'blog/single_post_page.html', # post 한 개를 sing~.html에 렌더링
        {
            'post' : post,
        }
    )
