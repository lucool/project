import os

from django.http import JsonResponse
from django.shortcuts import render


def ajax_upload_view(request):
    if request.method == "GET":
        return render(request,'ajax_app/ajax_upload.html')
    elif request.method == "POST":
        upload_author = request.POST.get("upload_author")  # 接收文本
        print("接收到的作者是：",upload_author)
        upload_file = request.FILES.get("upload_file")   # 接收上传文件
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        dest_path = os.path.join(BASE_DIR,'upload',upload_file.name)
        with open(dest_path,'wb') as f:
            for chunk in upload_file.chunks():   # 循环分块写入
                f.write(chunk)

        data = {
            "code":"201",
            "msg":"上传成功！",
            "path":"/static/" + upload_file.name +"/"
        }
        return JsonResponse(data)