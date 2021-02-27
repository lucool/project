from rest_framework.decorators import api_view
from rest_framework.response import Response

from drfapp.models import Toy
from drfapp.serializers import ToySerializer


@api_view(["GET","DELETE"])
def toy_view(request,toyid):
    try:
        toy = Toy.objects.get(pk=toyid)
    except Toy.DoesNotExist:
        data = {
            "code":"404",
            "msg":"没有该玩具！"
        }
        return Response(data)

    ser = ToySerializer(toy)
    if request.method == "GET":
        return Response(ser.data)
    elif request.method == "DELETE":
        toy.delete()
        return Response(ser.data)
