from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('feature/', views.feature, name='feature'),
    path('team/', views.team, name='team'),
    path('appointment/', views.appointment, name='appointment'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('contact/', views.contact, name='contact'),
    
]
