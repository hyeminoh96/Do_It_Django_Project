from django.urls import path
from . import views  # 현재 폴더에 있는 views.py를 사용할 수 있게 가져와랑

urlpatterns = [
    path('', views.index)  # 입력된 url이 'blog/'로 끝난다면 임포트한 views.py에 정의되어 있는 index() 함수를 실행
]
