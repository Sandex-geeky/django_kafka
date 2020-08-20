import json
import traceback
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.http import Http404

from core.models import TrafficLog

# Create your views here.

@csrf_exempt
def api_log(request):
    if request.method == 'POST':
        bin_data = request.body
        data = json.loads(bin_data.decode('utf-8'))
        print(data)
        try:
            TrafficLog.objects.create(user_id=data.get('user_id'), traffic_mb=data.get('traffic_mb'))
        except Exception as e:
            return HttpResponse(e)
        return JsonResponse(data, safe=False)

    elif request.method == 'GET':
        return HttpResponse("Traffic log API")
