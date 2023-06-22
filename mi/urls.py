from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('run-migrations', views.run_migrations, name='run_migrations')
]
