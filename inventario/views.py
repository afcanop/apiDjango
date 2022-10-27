from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import itemSerializers
from .repository.itemRepository import itemRepository

@csrf_exempt
def grupo_nuevo(request):
    if  request.method == "GET":
        print("asd")
