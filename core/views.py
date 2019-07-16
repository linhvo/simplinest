import json
import logging
import os

from django.http import Http404
from django.http import HttpResponse
import requests
from core.models import Location, NestAuth, Device
from django.shortcuts import render_to_response, render

logger = logging.getLogger(__name__)


def simplisafe_away(request):
    print('GET %s' % request.get_full_path())
    status_res = set_simplisafe_state('away')
    if not status_res:
        return Http404('No Location Id')
    return HttpResponse(status_res, content_type="application/json")


def set_simplisafe_state(state):
    cookie_dict, uid, session_name = simplisafe_login()
    location_data = {"no_persist": 0, "XDEBUG_SESSION_START": session_name}
    location_resp = requests.post('https://simplisafe.com/mobile/%s/locations' % uid,
                                  data=location_data, cookies=cookie_dict)
    lid = None
    if location_resp.status_code == 200:
        print('Location Info: %s' % location_resp.json())
        for key in location_resp.json()['locations'].keys():
            if key:
                lid = Location.objects.get_or_create(lid=key)[0]
            else:
                print(location_resp.json())
                continue
    else:
        print('Error location:%s' % location_resp.status_code )


    if not lid:
        return None

    set_state = {"state": state, "mobile": 1, "no_persist": 0, "XDEBUG_SESSION_START": "session_name"}
    print('Setting state: %s', set_state)
    status_res = requests.post('https://simplisafe.com/mobile/%s/sid/%s/set-state' % (uid, lid.lid),
                               data=set_state, cookies=cookie_dict)
    return status_res


def simplisafe_login():
    logger.info('Logging in Simplisafe')
    login_request_data = {"name": os.environ.get('SIMPLISAFE_USERNAME'),
                    "pass": os.environ.get('SIMPLISAFE_PASSWORD'),
                    "device_uuid": "51644e80-1b62-11e3-b773-0800200c9a66",
                    "no_persist": 1,
                    "version": "1200"}

    login_info = requests.post('https://simplisafe.com/mobile/login/', data=login_request_data)
    data = login_info.json()

    uid = data.get('uid')
    session_name = data.get('session')

    cookie_key = login_info.cookies.keys()[1]
    cookie_value = login_info.cookies[cookie_key]
    cookie_dict = dict()
    cookie_dict[cookie_key] = cookie_value
    print('Login Info: %s, Cookie: %s' % (data, cookie_dict))
    return cookie_dict, uid, session_name


def home(request):
    return HttpResponse("login.html")


def set_vacation(request):
    active = request.GET['active']
    auth = NestAuth.objects.first()
    device = Device.objects.get(nest_auth=auth)
    if active == 'on':
        device.vacation_mode = True
        device.save()
        return HttpResponse('Turn On Vacation', status=200)
    else:
        if not device.vacation_mode:
            return HttpResponse('Vacation is off already', status=200)
        else:
            device.vacation_mode = False
            device.save()
            return HttpResponse('Turn Off Vacation', status=200)










