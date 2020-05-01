from datetime import timedelta

from django.http import HttpResponse
from django.utils import timezone

from django_q.models import Schedule
from django_q.tasks import schedule

DELAY = 5  # seconds
FILEPATH = '/tmp/file.txt'  # Change this if you're on MacOS


def schedule_view(request):
    what = 'core.views.do_something'
    when = timezone.now() + timedelta(seconds=DELAY)

    schedule(what, schedule_type=Schedule.ONCE, next_run=when)

    return HttpResponse(f'''
        <p>
            Something will be written to <pre>{FILEPATH}</pre> in {DELAY} sec.
        <p>
    ''')


def do_something():
    now = timezone.now()
    with open(FILEPATH, 'a') as fp:
        fp.write(f'[{now}]\tSomething very expected happened.\n')

