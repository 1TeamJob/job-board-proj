from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings


def contact(request):
    info = Info.objects.first()
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        
        send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER, ],
            fail_silently=False,
        )
        
    
    context = {'info': info}
    return render(request, 'contact/contact.html', context)
