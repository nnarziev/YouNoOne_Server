from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from Tools import extract_post_params
from user.models import Participant
from ema.models import Response
from . import models
import datetime

# region Constants
RES_SUCCESS = 0
RES_FAILURE = 1
RES_BAD_REQUEST = -1


# endregion


# Create your views here.
def user_exists(username):
    return models.Participant.objects.filter(username=username).exists()


def is_user_valid(username, password):
    if user_exists(username):
        user = models.Participant.objects.get(username=username)
        return user.password == password
    return False


@csrf_exempt
@require_http_methods(['POST'])
def register_api(request):
    try:
        params = extract_post_params(request)
        if 'username' in params and 'password' in params and 'phone_num' in params:
            username = params['username']
            phone = params['phone_num']
            password = params['password']
            if user_exists(username):
                return JsonResponse(data={
                    'result': RES_FAILURE, 'reason': 'username is taken'
                })
            else:
                new_participant = models.Participant(username=username, phone_num=phone, password=password, register_datetime=datetime.datetime.now().timestamp())
                new_participant.save()

                for i in range(1, 32):
                    ema_user_data = Response(username=new_participant, day_num=i)
                    ema_user_data.save()

                return JsonResponse(data={'result': RES_SUCCESS})
    except ValueError as e:
        print(str(e))
        return JsonResponse(data={'result': RES_BAD_REQUEST, 'reason': 'either username or phone number or password was not passed as a POST argument!'})



@csrf_exempt
@require_http_methods(['POST'])
def login_api(request):
    try:
        params = extract_post_params(request)
        if 'username' in params and 'password' in params:
            username = params['username']
            password = params['password']
            if is_user_valid(username, password):
                participant = Participant.objects.get(username=username)
                participant.last_login_datetime = datetime.datetime.now().timestamp()
                participant.save()
                return JsonResponse(data={'result': RES_SUCCESS})
            else:
                return JsonResponse(data={
                    'result': RES_FAILURE, 'reason': 'wrong credentials passed'
                })
    except ValueError as e:
        print(str(e))
        return JsonResponse(data={'result': RES_BAD_REQUEST, 'reason': 'Username or Password was not passed as a POST argument!'})


@csrf_exempt
@require_http_methods(['POST'])
def heartbeat_smartphone_api(request):
    try:
        params = extract_post_params(request)
        if 'username' in params and 'password' in params:
            username = params['username']
            password = params['password']
            if is_user_valid(username, password):
                participant = Participant.objects.get(username=username)
                participant.heartbeat_smartphone = datetime.datetime.now().timestamp()
                participant.save()
                return JsonResponse(data={'result': RES_SUCCESS})
            else:
                return JsonResponse(data={
                    'result': RES_FAILURE, 'reason': 'wrong credentials passed'
                })
    except ValueError as e:
        print(str(e))
        return JsonResponse(data={'result': RES_BAD_REQUEST, 'reason': 'Username or Password was not passed as a POST argument!'})


@csrf_exempt
@require_http_methods(['POST'])
def heartbeat_smartwatch_api(request):
    try:
        params = extract_post_params(request)
        if 'username' in params and 'password' in params:
            username = params['username']
            password = params['password']
            if is_user_valid(username, password):
                participant = Participant.objects.get(username=username)
                participant.heartbeat_smartwatch = datetime.datetime.now().timestamp()
                participant.save()
                return JsonResponse(data={'result': RES_SUCCESS})
            else:
                return JsonResponse(data={
                    'result': RES_FAILURE, 'reason': 'wrong credentials passed'
                })
    except ValueError as e:
        print(str(e))
        return JsonResponse(data={'result': RES_BAD_REQUEST, 'reason': 'Username or Password was not passed as a POST argument!'})
