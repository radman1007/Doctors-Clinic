from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from . import models

def index(request):
    teams = models.Team.objects.all()
    forms = models.Testimonial.objects.all()
    reserves = None
    day_reserves = models.ReservationDay.objects.all()
    if request.method == 'POST':
        day = request.POST.get('day')
        day = get_object_or_404(models.ReservationDay, date=day)
        time = request.POST.get('time')
        reserves = models.FreeReservation.objects.filter(day=day, is_reserved=False)
        form = forms.ReserveForm(request.POST)
        if form.is_valid():
            form.save()
            x = models.FreeReservation.objects.get(day=day, time=time)
            x.is_reserved=True
            x.save()
            return redirect('index')
    context = {
        'teams' : teams,
        'forms' : forms,
        'reserves' : reserves,
        'day_reserves' : day_reserves,
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
    reserves = None
    day_reserves = models.ReservationDay.objects.all()
    if request.method == 'POST':
        day = request.POST.get('day')
        day = get_object_or_404(models.ReservationDay, date=day)
        time = request.POST.get('time')
        reserves = models.FreeReservation.objects.filter(day=day, is_reserved=False)
        form = forms.ReserveForm(request.POST)
        if form.is_valid():
            form.save()
            x = models.FreeReservation.objects.get(day=day, time=time)
            x.is_reserved=True
            x.save()
            return redirect('index')
    context = {
        'tests' : tests,
        'reserves' : reserves,
        'day_reserves' : day_reserves,
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
    reserves = None
    day_reserves = models.ReservationDay.objects.all()
    if request.method == 'POST':
        day = request.POST.get('day')
        day = get_object_or_404(models.ReservationDay, date=day)
        time = request.POST.get('time')
        reserves = models.FreeReservation.objects.filter(day=day, is_reserved=False)
        form = forms.ReserveForm(request.POST)
        if form.is_valid():
            form.save()
            x = models.FreeReservation.objects.get(day=day, time=time)
            x.is_reserved=True
            x.save()
            return redirect('index')
    context = {
        'reserves' : reserves,
        'day_reserves' : day_reserves,
    }
    return render(request, 'appointment.html', context)

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
