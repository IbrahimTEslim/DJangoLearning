from django.shortcuts import render
from .models import job

# Create your views here.

def job_lists(request):
    job_list = job.objects.all().order_by('id')
    print(job_list)
    context = {'jobs' : job_list}
    return render(request,'job/job_lists.html',context)

def job_details(request,id):
    job_detail = job.objects.get(id=id)
    context = {'job' : job_detail}
    return render(request,'job/job_detail.html',context)
