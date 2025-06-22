from django.db import models


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)
    
    class Meta:
        abstract = True
