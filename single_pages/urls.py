from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.about_me), # about_me가 url에 붙어있으면 about_me()함수 실행
    path('', views.landing), # 아무것도 붙어있지 않으면 landing() 실햄
]