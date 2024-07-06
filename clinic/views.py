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
    return render(request, 'team.html', context)

def appointment(request):
    return render(request, 'appointment.html')

def testimonial(request):
    forms = Testimonial.objects.filter()
    context = {
        'forms' : forms
    }
    return render(request, 'testimonial.html', context)

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
    return render(request, 'contact.html', context)
