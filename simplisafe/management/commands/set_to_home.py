from django.core.management import BaseCommand
import requests

from core.models import NestAuth, Device


class Command(BaseCommand):
    help = 'Set thermostate to home'

    def handle(self, *args, **options):
        auth = NestAuth.objects.first()
        if not auth:
            return 
        if not auth.access_token:
            access_token = self.get_access_token(auth)
            auth.access_token = access_token
            auth.save()


        device = Device.objects.get(nest_auth=auth)
        structure_id = device.structure_id
        url = "https://developer-api.nest.com/structures/%s/away?auth=%s" % (structure_id, auth.access_token)
        res = requests.put(url, content_type='application/json', data="home")
        print (res.status_code, res.json())

    def get_access_token(self, auth):
        auth_code = auth.auth_code
        client_id = auth.client_id
        client_secret = auth.client_secret
        request_token_url = 'https://api.home.nest.com/oauth2/access_token?' \
                            'client_id=%s&code=%s&client_secret=%s' \
                            '&grant_type=authorization_code' % (client_id, auth_code, client_secret)

        resp = requests.post(request_token_url)
        return resp.json()['access_token']