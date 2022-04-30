from django.shortcuts import render, redirect
from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyForm
from django.urls import reverse


def job_list(request):
    job_list = Job.objects.all()
    paginator = Paginator(job_list, 5) # Show 5 Jobs Per Page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs': page_obj}
    print(job_list)
    return render(request, 'job/job_list.html', context)



def job_details(request, slug):
    job_details = Job.objects.get(slug=slug)
    
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form. is_valid():
            my_form = form.save(commit=False)
            my_form.job = job_details
            my_form.save()
            return redirect(reverse('jobs:job_list'))
    
    else:
        form = ApplyForm

    context = {'job': job_details, 'form': form}
    return render(request, 'job/job_details.html', context)