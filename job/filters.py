import django_filters
from .models import Job


class Job_Filter(django_filters.FilterSet):
    
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Job
        fields = ['title', 'job_type', 'experience', 'description', 'category']
