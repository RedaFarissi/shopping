# from django.db import models
# from django.contrib.auth.models import User
# from django.urls import reverse



# # Create your models here.
# class Store(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     image = models.ImageField(upload_to='store_profile/%Y/%m/%d', verbose_name="image store", blank=True)
#     slug = models.SlugField(max_length=50)
#     created = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['name']
#         indexes = [
#             models.Index(fields=['id', 'slug']),
#             models.Index(fields=['name']),
#             models.Index(fields=['-created']),
#         ]
#     def __str__(self):
#        return self.name
    
#     def get_absolute_url(self):
#         return reverse('store_list' , args=[self.slug])