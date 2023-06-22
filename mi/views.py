from datetime import datetime

from django.http import HttpResponse

from . import models


def index(request):
    t = models.Person()
    t.first_name = 'igor'
    t.last_name = 'trentini'
    t.birth_date = datetime.today()

    return HttpResponse(t)


def other(request):
    return HttpResponse('outro :)')
