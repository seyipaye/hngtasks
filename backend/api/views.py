from enum import Enum
from django.http import JsonResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4


@csrf_exempt
def api_home(request, *args, **kwargs):
    body = request.body
    api_response = {}
    try:
        api_response = json.loads(body)
    except:
        pass
    print(body)
    return JsonResponse(api_response)