from django.urls import path
from . import views  # 현재 폴더에 있는 views.py를 사용할 수 있게 가져와랑

urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()), # as_view(해당 뷰에게 전달될 인자)
    path('', views.PostList.as_view()) # url이 /blog/로 끝나면 PostList 클래스로 처리함

    # ---- FBV ---
    # path('', views.index)  # 입력된 url이 blog/ 뒤에 아무것도 없다면 임포트한 views.py에 정의되어 있는 index() 함수를 실행
    # path('blog/<int:pk>/', views.single_post_page), # url이 blog/(int)이면 single_post_page() 함수를 실행
]
