from django.urls import path
from accounts import views

# namespace가 accounts라는 이름을 가졌음을 명시
app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('temp/', views.temp, name='temp'),  # temp 뷰에 대한 URL 패턴 추가
]