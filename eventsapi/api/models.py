from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now


class Event(models.Model):
    title = models.CharField(max_length=150)
    created = models.DateTimeField(default=now)
