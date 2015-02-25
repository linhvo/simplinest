import json
import logging
import os
import datetime
from django.dispatch import receiver
from django.http import HttpResponse
import requests
import oauth2 as oauth
from core.models import User, Location
from django.db.models.signals import pre_save

logger = logging.getLogger(__name__)


def simplisafe_away(request):
    cookie_dict, uid = simplisafe_login()
    location_data = {"no_persist": 1, "XDEBUG_SESSION_START": "session_name"}
    location_resp = requests.post('https://simplisafe.com/mobile/%s/locations' % uid,
                         data=location_data, cookies=cookie_dict)
    for key in json.loads(location_resp.content)['locations'].keys():
        if key:
            try:
                lid = Location(lid = key)
                lid.save()
            except Exception as ex:
                logger.error(ex)


    lid = Location.objects.first().lid
    set_away_data = {"state": "away", "mobile": 1, "no_persist": 1, "XDEBUG_SESSION_START": "session_name"}

    status_res = requests.post('https://simplisafe.com/mobile/%s/sid/%s/set-state' % (uid, lid),
                              data=set_away_data, cookies=cookie_dict)
    return HttpResponse(status_res, content_type="application/json")


def simplisafe_login():
    login_request_data = {"name": os.environ.get('SIMPLISAFE_USERNAME'),
                    "pass": os.environ.get('SIMPLISAFE_PASSWORD'),
                    "device_uuid": "51644e80-1b62-11e3-b773-0800200c9a66",
                    "no_persist": 1,
                    "version": "1200"}

    location_resp = requests.post('https://simplisafe.com/mobile/login/', data=login_request_data)
    data = json.loads(location_resp.content)
    uid = data['uid']

    cookie_key = location_resp.cookies.keys()[1]
    cookie_value = location_resp.cookies[cookie_key]
    cookie_dict = dict()
    cookie_dict[cookie_key] = cookie_value
    return cookie_dict, uid




