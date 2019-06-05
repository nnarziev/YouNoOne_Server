from django.http import JsonResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import datetime

from Tools import extract_post_params
from user.models import Participant
import io
import csv
from . import models
from user.views import RES_SUCCESS
from user.views import RES_FAILURE
from user.views import RES_BAD_REQUEST

# region Constants
DEVICE_TYPE_WATCH = "smartwatch"
DEVICE_TYPE_PHONE = "smartphone"
DATA_SRC_ACC = "1"
DATA_SRC_STATIONARY_DUR = "2"
DATA_SRC_SIGNIFICANT_MOTION = "3"
DATA_SRC_STEP_DETECTOR = "4"
DATA_SRC_UNLOCKED_DUR = "5"
DATA_SRC_PHONE_CALLS = "6"
DATA_SRC_LIGHT = "7"
DATA_SRC_APP_USAGE = "8"
DATA_SRC_HRM = "9"


# endregion

# Create your views here.
def user_exists(username):
    return Participant.objects.filter(username=username).exists()


def is_user_valid(username, password):
    if user_exists(username):
        participant = Participant.objects.get(username=username)
        return participant.password == password
    return False


@csrf_exempt
@require_http_methods(['POST'])
def submit_api(request):
    try:
        params = extract_post_params(request)
        if 'username' not in params or 'password' not in params or 'file' not in request.FILES:
            raise ValueError('username/password/file is not in request params')
        if not is_user_valid(params['username'], params['password']):
            return JsonResponse({'result': RES_FAILURE})
        else:
            username = params['username']
            participant = Participant.objects.get(username=username)

            csv_file = request.FILES['file']
            device_name = csv_file.name.split('_')[0]
            data_set = csv_file.read().decode('UTF-8')

            # region Precessing the received data
            print("User: ", username, ";\tsource: ", device_name)
            print("File: ", csv_file.name, ";\tsize: ", len(data_set) / 1024)
            io_string = io.StringIO(data_set)
            for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                data_src = column[0]
                timestamp = column[1]
                values = column[2]

                if data_src == DATA_SRC_ACC:
                    val_x, val_y, val_z = values.split(" ")
                    new_raw_data = models.acc(username=participant, timestamp=timestamp, value_x=val_x, value_y=val_y, value_z=val_z, device=device_name)
                    new_raw_data.save()
                elif data_src == DATA_SRC_STEP_DETECTOR:
                    new_raw_data = models.step_detector(username=participant, timestamp=timestamp, device=device_name)
                    new_raw_data.save()
                elif data_src == DATA_SRC_SIGNIFICANT_MOTION:
                    new_raw_data = models.significant_motion(username=participant, timestamp=timestamp, device=device_name)
                    new_raw_data.save()
                elif data_src == DATA_SRC_STATIONARY_DUR:
                    new_raw_data = models.stationary_dur(username=participant, timestamp_endtime=timestamp, duration=values, device=device_name)
                    new_raw_data.save()
                elif data_src == DATA_SRC_UNLOCKED_DUR:
                    new_raw_data = models.unlocked_dur(username=participant, timestamp_endtime=timestamp, duration=values, device=device_name)
                    new_raw_data.save()
                elif data_src == DATA_SRC_PHONE_CALLS:
                    call_type, duration = values.split("/")
                    new_raw_data = models.phone_calls(username=participant, timestamp=timestamp, call_type=call_type, duration=duration, device=device_name)
                    new_raw_data.save()
                elif data_src == DATA_SRC_LIGHT:
                    new_raw_data = models.light_intensity(username=participant, timestamp=timestamp, value=values, device=device_name)
                    new_raw_data.save()
                elif data_src == DATA_SRC_APP_USAGE:
                    app_name, duration = values.split("|")
                    new_raw_data = models.app_usage(username=participant, timestamp=timestamp, app_name=app_name, value=duration, device=device_name)
                    new_raw_data.save()
                elif data_src == DATA_SRC_HRM:
                    new_raw_data = models.hrm(username=participant, timestamp=timestamp, value=values, device=device_name)
                    new_raw_data.save()
            # endregion

            # region Setting amount of data loaded by user
            cur_datetime = datetime.datetime.now()
            last_heart_beat_phone = datetime.datetime.fromtimestamp(participant.heartbeat_smartphone)
            last_heart_beat_watch = datetime.datetime.fromtimestamp(participant.heartbeat_smartwatch)

            if device_name == DEVICE_TYPE_PHONE:
                if cur_datetime.day == last_heart_beat_phone.day:
                    participant.daily_data_size_smartphone = participant.daily_data_size_smartphone + (len(data_set) / 1024)
                else:
                    participant.daily_data_size_smartphone = len(data_set) / 1024
            elif device_name == DEVICE_TYPE_WATCH:
                if cur_datetime.day == last_heart_beat_watch.day:
                    participant.daily_data_size_smartwatch = participant.daily_data_size_smartwatch + (len(data_set) / 1024)
                else:
                    participant.daily_data_size_smartwatch = len(data_set) / 1024
            participant.save()
            # endregion

            return JsonResponse(data={'result': RES_SUCCESS})
    except ValueError as e:
        print(e)
        return JsonResponse({'result': RES_BAD_REQUEST})
