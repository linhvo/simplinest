import logging
from django.core.management import BaseCommand

from core.models import Device, NestAuth
from core.views import set_simplisafe_state

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Turn on alarm at 11:30'

    def handle(self, *args, **options):
        auth = NestAuth.objects.first()
        device = Device.objects.get(nest_auth=auth)
        if device.vacation_mode:
            print('In vacation mode, do not change state')
            return

        print('Turning on alarm')
        res = set_simplisafe_state('home')
        if not res:
            print("Cannot turn on alarm")
