from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE


class Status(SafeDeleteModel, models.Model):
    _safedelete_policy = SOFT_DELETE

    name = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
