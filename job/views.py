from django.shortcuts import render


def job_list(request):
    context = {}
    return render(request, 'job/job_list.html', context)


def job_details(request):
    context = {}
    return render(request, 'job/job_details.html', context)
