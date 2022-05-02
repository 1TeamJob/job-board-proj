from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.ForeignKey('address', on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.user)
    
    
# when Craete New User --> create user profile manually.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    

class Address(models.Model):
    address = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.address
