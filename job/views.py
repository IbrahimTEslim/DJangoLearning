from django.shortcuts import redirect, render
from .models import job
from django.core.paginator import Paginator
from .form import ApplyForm, PostJob
from django.urls import reverse


# Create your views here.

def job_lists(request):
    job_list = job.objects.all().order_by('id')
    paginator = Paginator(job_list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs' : page_obj}
    return render(request,'job/job_lists.html',context)

def job_details(request,slug):
    job_detail = job.objects.get(slug=slug)
    

    if request.method=='POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid:
            myForm = form.save(commit=False)
            myForm.jobID = job_detail
            myForm.save()
    else:
        form = ApplyForm()

    context = {'job' : job_detail,'form':form }
    
    return render(request,'job/job_detail.html',context)


def job_add(request):
    if request.method == 'POST':
        postForm = PostJob(request.POST, request.FILES)
        if postForm.is_valid:
            myPostForm = postForm.save(commit=False)
            myPostForm.owner = request.user
            myPostForm.save()
            return redirect(reverse('jobs:job_list'))
    else:
        myPostForm = PostJob
            
    return render(request,'job/add_job.html',{'form':myPostForm})
 