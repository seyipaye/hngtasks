from enum import Enum
from django.http import JsonResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

#{"operation_type":"What is the difference of","x":5,"y":20}
#b'{"operation_type":"subtraction","x":10,"y":2}'

#{ “slackUsername”: String, “result”: Integer, “operation_type”: Enum.value }

# Recieve request
# Tell if it is multipliction or Addition or subtraction
# Return a response with the value

@csrf_exempt
def api_home(request, *args, **kwargs):
    x = 0
    y = 0
    operation_type = None

    body = request.body
    api_response = {}
    try:
        x = json.loads(body)['x']
        y = json.loads(body)['y']
        operation_type = my_function(json.loads(body)['operation_type'])
    except:
        pass
    print(body)

    #if operation_type == None:
    return JsonResponse({'slackUsername' : 'seyipaye', 'operation_type': operation_type.name, 'result': get_result(operation_type, x, y)})

def get_result(operation, x, y):
    match operation:
        case Enum.addition:
            return x + y
        case Enum.subtraction:
            return x - y
        case Enum.multiplication:
            return x * y
    


def my_function(data):
    addition = ['add', 'sum', 'plus', 'addition', 'summation']
    subtraction = ['subtract', 'difference', 'minus', 'subtraction']
    multiplication = ['multiply', 'product', 'times', 'multiplication']

    if any(value in data for value in addition):
        return Enum.addition
    elif any(value in data for value in subtraction):
        return Enum.subtraction
    elif any(value in data for value in multiplication):
        return Enum.multiplication
    else: 
        return None

class Enum(Enum):
    addition = 'Enum.addition'
    subtraction = 'Enum.subtraction'
    multiplication = 'Enum.multiplication'
 