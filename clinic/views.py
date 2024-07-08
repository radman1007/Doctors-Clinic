from django.shortcuts import render, redirect
from . import forms
from . import models

def index(request):
    teams = models.Team.objects.all()
    forms = models.Testimonial.objects.all()
    context = {
        'teams' : teams,
        'forms' : forms,
    }
    return render(request, 'index.html', context)

def about(request):
    teams = models.Team.objects.all()
    context = {
        'teams' : teams
    }
    return render(request, 'about.html', context)

def service(request):
    tests = models.Testimonial.objects.all()
    if request.method == 'POST':
        form = forms.ReserveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'tests' : tests
    }
    return render(request, 'service.html', context)
    
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
    forms = models.Testimonial.objects.all()
    context = {
        'forms' : forms
    }
    return render(request, 'testimonial.html', context)

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
