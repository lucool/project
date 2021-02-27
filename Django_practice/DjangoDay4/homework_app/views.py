from django.http import JsonResponse
from django.shortcuts import render


def go_fruits(request):
    return render(request,'homework_app/fruits.html')


def send_fruits(request):
    #fruits = ["苹果","香蕉","橘子","菠萝"]
    fruits = [
        {
            "id":1,
            "name":"苹果",
            "price":12.5
        },
        {
            "id": 2,
            "name": "香蕉",
            "price": 20
        },
        {
            "id": 3,
            "name": "橘子",
            "price": 5
        },
    ]
    return JsonResponse(fruits,safe=False)