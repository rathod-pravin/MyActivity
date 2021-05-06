from django.db import models
import datetime

class MyTask(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.CharField(default='Pravin', max_length=100)
    create_date = models.DateField(default=datetime.date.today(), editable=False)
    is_done = models.BooleanField(default=False, blank=True, null=True)
    objects = models.Manager()
    def __str__(self):
        return self.name
