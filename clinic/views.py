from django.shortcuts import render, redirect
from . import forms
from . import models

def index(request):
    teams = models.Team.objects.all()
    context = {
        'teams' : teams
    }
    return render(request, 'index.html', context)

def about(request):
    teams = models.Team.objects.all()
    context = {
        'teams' : teams
    }
    return render(request, 'about.html', context)

def service(request):
    return render(request, 'service.html')
    
def feature(request):
    return render(request, 'feature.html')

def team(request):
    teams = models.Team.objects.all()
    context = {
        'teams' : teams
    }
    return render(request, 'team.html', context)

def appointment(request):
    return render(request, 'appointment.html')

def testimonial(request):
    forms = models.Testimonial.objects.filter()
    context = {
        'forms' : forms
    }
    return render(request, 'testimonial.html')

def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    form = forms.ContactForm()
    context = {
        'form' : form,
    }
    return render(request, 'contact.html', context)
