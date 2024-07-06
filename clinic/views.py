from django.shortcuts import render, redirect
from .forms import ContactForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')
    
def feature(request):
    return render(request, 'feature.html')

def team(request):
    return render(request, 'team.html')

def appointment(request):
    return render(request, 'appointment.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    form = ContactForm()
    context = {
        'form' : form,
    }
    return render(request, 'contact.html')
