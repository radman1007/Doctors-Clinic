from django import forms
from . import models

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = '__all__'
        
        
class ReserveForm(forms.ModelForm):
    class Meta:
        model = models.Reservation
        fields = '__all__'