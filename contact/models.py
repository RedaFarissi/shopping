from django.db import models
from django.urls import reverse



class ContactUser(models.Model):
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    contact_date = models.DateTimeField(auto_now=True)
    vu = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
    
    def get_absolute_url(self):
        return reverse('reply_to_the_user' , args=[self.email , self.pk])