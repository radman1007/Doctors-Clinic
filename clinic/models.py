from django.db import models
from django.utils.translation import gettext_lazy as _

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
    instagram = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.name


class ReservationDay(models.Model):
    date = models.DateField(_("Date"))
    
    class Meta:
        verbose_name = _("Reservation Day")
        verbose_name_plural = _("Reservation Days")
        ordering = ('-date',)
        
    def __str__(self):
        return self.date
    
    
DOCTOR_CHOICES = (
    ('D1', 'Doctor1'),
    ('D2', 'Doctor2'),
    ('D3', 'Doctor3'),
)
    
    
class Reservation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=12)
    doctor = models.CharField(max_length=255, choices=DOCTOR_CHOICES, default='D1')
    text = models.TextField()
    day = models.ForeignKey(ReservationDay, on_delete=models.CASCADE, verbose_name=_("Day"), related_name='reservation')
    time = models.TimeField(_('Time'))
    
    class Meta:
        verbose_name = _("Reservation")
        verbose_name_plural = _("Reservations")
        ordering = ('time',)
        
    def __str__(self):
        return f"{self.name} : {self.day} - {self.time}"