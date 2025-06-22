from django.db import models

from common import BaseModel


class Runtime(BaseModel):
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)


class Function(BaseModel):
    name = models.CharField(max_length=255)
    decsription = models.TextField()
    code = models.TextField()
    runtime = Runtime()
    is_active = models.BooleanField(default=True)
