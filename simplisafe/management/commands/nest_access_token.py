from core.models import NestAuth
from django.core.management import BaseCommand
import requests
import json
from django.http import HttpResponse


class Command(BaseCommand):
    def handle(self, *args, **options):
        get_access_token()


def get_access_token():
    auth = NestAuth.objects.first()
    auth_code = auth.auth_code
    client_id = auth.client_id
    client_secret = auth.client_secret
    request_token_url = 'https://api.home.nest.com/oauth2/access_token?' \
                        'client_id=%s&code=%s&client_secret=%s' \
                        '&grant_type=authorization_code' % (client_id, auth_code, client_secret)

    resp = requests.post(request_token_url)
    content = json.loads(resp.content)
    auth.access_token = content['access_token']
    auth.save()
    return HttpResponse(content, content_type="application/json")
