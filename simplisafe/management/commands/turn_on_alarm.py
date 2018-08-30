import logging
from django.core.management import BaseCommand

from core.views import set_simplisafe_state

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Turn on alarm at 11:30'

    def handle(self, *args, **options):
        print('Turning on alarm')
        // res = set_simplisafe_state('home')
        // print(res.json())
