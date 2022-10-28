from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from inventario.serializers import itemSerializers
from inventario.repository.grupoRepository import grupoRepository


@csrf_exempt
def grupo_nuevo(request):
    if request.method == "GET":
        objGrupoRepository = grupoRepository()
        objGrupoRepository.nuevo()
        return JsonResponse({"elemento Registrado": 200}, safe=False)
