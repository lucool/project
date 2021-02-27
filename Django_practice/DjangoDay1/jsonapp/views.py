from django.http import JsonResponse
from django.shortcuts import render


def json_object_view(request):
    data = {
        "name":"tom",
        "age":20,
        "score":90.5
    }
    return JsonResponse(data)


def json_array_view(request):
    data = [
        {
            "name": "tom",
            "age": 20,
            "score": 90.5
        },
        {
            "name": "alice",
            "age": 25,
            "score": 62
        }
    ]
    return JsonResponse(data,safe=False)
