from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from inventario.serializers import itemSerializers
from inventario.repository.itemRepository import itemRepository


@csrf_exempt
def item_lista(request):
    if request.method == "GET":
        objItemRepository = itemRepository()
        arrItems = itemSerializers(objItemRepository.lista(), many=True)
        return JsonResponse(arrItems.data, safe=False)


@csrf_exempt
def item_detalle(request):
    if request.method == "GET":
        objItemRepository = itemRepository()
        arrItems = itemSerializers(objItemRepository.detalle())
        return JsonResponse(arrItems.data)

@csrf_exempt
def item_nuevo(request):
    if request.method == "GET":
        print(request)
        objItemRepository = itemRepository()
        objItemRepository.nuevo()
        return JsonResponse({ "elemento Registrado": 200}, safe=False)
