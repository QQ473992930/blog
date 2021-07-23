from django.urls import path
from users.views import RegisterView,ImageCodeView

urlpatterns=[
    #第一个参数 路由
    #第二个参数 视图函数名
    path('register/',RegisterView.as_view(),name='register'),
    path('imagecode/',ImageCodeView.as_view(),name='imagecode'),
]