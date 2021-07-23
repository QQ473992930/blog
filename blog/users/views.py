from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http.response import HttpResponseBadRequest,HttpResponse
#注册视图
from libs.captcha.captcha import captcha
from django_redis import get_redis_connection


class RegisterView(View):

    def get(self,request):
        return  render(request,'register.html')

class ImageCodeView(View):

    def get(self,request):

        # 1 接受前端的uuid
        uuid =request.GET.get('uuid')
        # 2判断uuid是否接收到
        if uuid is None:
            return HttpResponseBadRequest('没有传递uuid')
        # 3通过调用captcha来生成图片验证码（图片二进制，和图片内容）
        text,image=captcha.generate_captcha()
        # 4将图片内容保存到redis中
        #     uuid作为key，图片内容作为value，同时设置一个时效
        redis_conn = get_redis_connection()
        redis_conn.setex=('img:%s'%uuid,300,text)
        # 5返回图片二进制
        return HttpResponse(image,content_type='image/jpeg')

