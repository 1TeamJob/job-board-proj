from django.db import models


class Info(models.Model):
    place = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField(max_length=100)   


    def __str__(self):
        return self.email
