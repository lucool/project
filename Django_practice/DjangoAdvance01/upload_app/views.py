import os

from django.shortcuts import render, redirect
from django.urls import reverse


def form_upload(request):
    if request.method == "GET":
        return render(request,'upload_app/upload_form.html')
    elif request.method == "POST":
        author = request.POST.get("author")
        print("上传人为：",author)
        upload_file = request.FILES.get("pic")   #  接收上传文件对象
        UPLOAD_DIR = os.path.dirname(os.path.abspath(__file__))
        dest_path = os.path.join(UPLOAD_DIR,'upload',upload_file.name)   #  拼接上传文件的最终路径
        with open(dest_path,'wb') as f:
            for chunk in upload_file.chunks():   # 将文件对象分块循环写入目标文件
                f.write(chunk)
        return redirect(reverse("up:suc",args=(upload_file.name,)))  # 重定向到成功页面，并传递参数


def success_view(request,path):
    return render(request,'upload_app/success.html',locals())