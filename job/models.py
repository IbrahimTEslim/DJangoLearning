from django.db import models
from django.db.models.base import Model
# from time import timezone
from datetime import datetime

# Create your models here.
JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time', 'Part Time'),
)

class job(models.Model):
    title = models.CharField(max_length=200)
    job_type = models.CharField(max_length=15,choices=JOB_TYPE,null=False)
    decscription = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experiance = models.IntegerField(default=1)

    def __str__(self):
        return self.title

