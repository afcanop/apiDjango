from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from inventario.serializers import itemSerializers
from inventario.repository.itemRepository import itemRepository


@csrf_exempt
def item_lista(request):
    if request.method == "GET":
        itemRepository2 = itemRepository()
        arrItems = itemSerializers(itemRepository2.lista(), many=True)
        return JsonResponse(arrItems.data, safe=False)


@csrf_exempt
def item_detalle(request):
    if request.method == "GET":
        itemRepository2 = itemRepository()
        arrItems = itemSerializers(itemRepository2.detalle())
        return JsonResponse(arrItems.data)