from django.shortcuts import render
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html', context)

def service(request):
    return render(request, 'service.html', context)
    
def feature(request):
    return render(request, 'feature.html')

def team(request):
    return render(request, 'team.html')

def appointment(request):
    return render(request, 'appointment.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def contact(request):
    return render(request, 'contact.html')
