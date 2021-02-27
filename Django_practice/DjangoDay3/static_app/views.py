from django.shortcuts import render


def show_view(request):
    return render(request,'static_app/show_girl.html')