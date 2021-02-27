from django.shortcuts import render


def go_a(request):
    return render(request,'homework_app/a.html')


def handle_a(request,hobby):
    return render(request,'homework_app/success_a.html',{"hobby":hobby})


def fruit_view(request):
    fruits = ["苹果","菠萝","橙子","橘子"]
    return render(request,'homework_app/fruits.html',{"fruits":fruits})


def sports_view(request,info):
    if info == "allsports":
        sports = ["足球","跑步","太极","羽毛球"]
    else:
        sports = []
    return render(request,'homework_app/sports.html',{"sports":sports})


def custom_view(request):
    mydict = {
        "sport": "football",
    }
    return render(request,'homework_app/custom_filter.html', locals())


