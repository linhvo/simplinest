from django.core.management import BaseCommand
import requests
import json
from django.http import HttpResponse

from core.models import NestAuth


class Command(BaseCommand):
    help = 'Set thermostate to home'
    def handle(self, *args, **options):
        auth = NestAuth.objects.first()
        auth_code = auth.auth_code
        client_id = auth.client_id
        client_secret = auth.client_secret
        request_token_url = 'https://api.home.nest.com/oauth2/access_token?' \
                            'client_id=%s&code=%s&client_secret=%s' \
                            '&grant_type=authorization_code' % (client_id, auth_code, client_secret)

        resp = requests.post(request_token_url)
        content = resp.json()['access_token']
        auth.access_token = content['access_token']
        auth.save()
        url = "https://developer-api.nest.com/structures/g-9y-2xkHpBh1MGkVaqXOGJiKOB9MkoW1hhYyQk2vAunCK8a731jbg/away?auth=<AUTH_TOKEN>"
        # curl - v - L - X
        # PUT
        # "https://developer-api.nest.com/structures/g-9y-2xkHpBh1MGkVaqXOGJiKOB9MkoW1hhYyQk2vAunCK8a731jbg/away?auth=<AUTH_TOKEN>" - H
        # "Content-Type: application/json" - d
        # '"away"'
