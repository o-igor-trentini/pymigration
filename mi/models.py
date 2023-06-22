from django.db import models


class Migrations(models.Model):
    class Meta:
        managed = False

    name = models.CharField(max_length=50)
    observation = models.CharField(max_length=255)
    created_at = models.DateTimeField()


class Person(models.Model):
    class Meta:
        managed = False

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateTimeField()
    blabla = models.DateTimeField()
