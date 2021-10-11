from django.db import models
from django.db.models.base import Model
# from time import timezone
from datetime import datetime
from django.db.models.deletion import CASCADE

from django.db.models.fields.related import ForeignKey
from django.http import request
from django.utils.text import slugify

from django.contrib.auth.models import User

# Create your models here.
JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time', 'Part Time'),
)

def upload_image(instance,filename):
    imageName , extension = filename.split(".")
    print("Instance Type: ",type(instance))
    print("Filename Type: ",type(filename))
    # print("Testoo Type: ",type(testoo))
    return "jobs/%s/%s.%s"%(instance.id,instance.id,extension)


class job(models.Model):
    owner = models.ForeignKey(User, related_name=("job_owner"), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    job_type = models.CharField(max_length=15,choices=JOB_TYPE,null=False)
    decscription = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experiance = models.IntegerField(default=1)
    category = ForeignKey('category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_image)
    slug = models.SlugField(blank=True,null=True)

    def save(self,*args,**kwargs): 
        self.slug = slugify(self.title)
        super(job,self).save(*args,**kwargs)
        
    def __str__(self):
        return self.title


class category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Apply(models.Model):
    jobID = models.ForeignKey(job,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    website = models.URLField()
    cv = models.FileField(upload_to='Apply/')
    cover_letter = models.TextField(max_length=1500)
    applied_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    

