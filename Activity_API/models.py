from django.db import models

class MyTask(models.Model):
    name = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False, blank=True,       null=True)
    objects = models.Manager()
    def __str__(self):
        return self.name
