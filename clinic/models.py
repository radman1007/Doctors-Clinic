from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    accept = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_date']
    def __str__(self):
        return self.name
    
    
class Testimonial(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class Team(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255, null=True)
    twitter = models.CharField(max_length=255, null=True)
    facebook = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.name