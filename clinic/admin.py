from django.contrib import admin
from . import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'email', 'message', 'created_date')
    list_filter = ('email',)
    search_fields = ('name', 'message')
    

@admin.register(models.Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'subject')
    
  
@admin.register(models.Team)  
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')
    search_fields = ('name', 'department')
    

class InlineReservation(admin.StackedInline):
    model = models.FreeReservation
@admin.register(models.ReservationDay)
class ReservationDateAdmin(admin.ModelAdmin):
    list_display = ('date',)
    inlines = (InlineReservation,)

@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'day', 'time')
