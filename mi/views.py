from django.http import HttpResponse
from django.utils import timezone
from mi.migrations.mymigrations import migration_20230622135520

from . import models


def index(request):
    t = models.Person()
    t.first_name = 'Igor'
    t.last_name = 'Trentini'
    t.birth_date = timezone.now()

    return HttpResponse(t)


def run_migrations(request):
    try:
        migrations = list([
            migration_20230622135520.migration_20230622135520,
        ])

        for migration in migrations:
            migration()

        return HttpResponse('Deu boa :)')

    except Exception as e:
        return HttpResponse("Ocorreu um erro:", str(e))
