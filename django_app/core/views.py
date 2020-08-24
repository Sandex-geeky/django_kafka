import json
import traceback
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.http import Http404
from django.contrib.auth import get_user_model

from core.models import TrafficLog
from core.tasks import calc_money

# Create your views here.

@csrf_exempt
def api_log(request):
    if request.method == 'POST':
        bin_data = request.body
        data = json.loads(bin_data.decode('utf-8'))
        try:
            user = get_user_model().objects.get(id=data.get('user_id'))
            TrafficLog.objects.create(user=user, traffic_mb=data.get('traffic_mb'))
            calc_money.delay(**data)
        except Exception as e:
            return HttpResponse(e)
        return JsonResponse(data, safe=False)

    elif request.method == 'GET':
        return HttpResponse("Traffic log API")
