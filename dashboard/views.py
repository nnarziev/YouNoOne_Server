from django.shortcuts import render
from user.models import Participant
from ema.models import Response
from datetime import datetime


# Create your views here.
def index(request):
    participants = Participant.objects.order_by('register_datetime')[:30]
    context = {
        'participants': participants
    }
    return render(request=request, template_name='index.html', context=context)


def ema(request):
    ema_responses = Response.objects.order_by('day_num')[:620]
    context = {
        'ema_responses': ema_responses
    }
    return render(request=request, template_name='ema.html', context=context)
