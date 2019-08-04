import logging
from django.core.management import BaseCommand

from core.models import Device
from core.views import set_simplisafe_state

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Turn on alarm at 11:30'

    def handle(self, *args, **options):
        if Device.vacation_mode:
            print('Vacation')
            return

        print('Turning on alarm')
        res = set_simplisafe_state('home')
        if not res:
            print("Cannot turn on alarm")
