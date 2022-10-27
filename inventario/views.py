from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import item
from .serializers import itemSerializers


@csrf_exempt
def item_lista(request):
    """
    lista de datos
    :param request:
    :return: json de items
    """

    if request.method == "GET":
        items = item.objects.all()

        arrItems = itemSerializers(items, many=True)

        print(items)

        return JsonResponse(arrItems.data, safe=False)

