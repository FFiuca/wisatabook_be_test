from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from master import models as m_master
import calendar

class Task(SafeDeleteModel, models.Model):
    _safedelete_policy = SOFT_DELETE

    class Meta:
        ordering=['-created_at']

    status = models.ForeignKey(
        m_master.Status,
        on_delete=models.CASCADE,
        default=1,
        related_name='status_task'
    )

    title = models.CharField(max_length=100, blank=False)
    starred_status  = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class TaskRepeat(models.Model):

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='task_to_task_repeat'
    )

    day = models.CharField(
        max_length=100,
        choices=[(i, i)for i in list(calendar.day_name)],
        blank=False
    )

