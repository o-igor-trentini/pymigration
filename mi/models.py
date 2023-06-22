from django.db import models


class Person(models.Model):
    class Meta:
        managed = False

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateTimeField()
