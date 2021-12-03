from django.db import models
from datetime import datetime


# Create your models here.

class Contactus(models.Model):
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, blank=True)
    subject = models.TextField()
    message = models.TextField()
    created_at = models.DateTimeField(blank=True, default=datetime.now)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.email

