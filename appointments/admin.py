from django.contrib import admin
from api.models import Appointments
from .models import Appointment
# Register your models here.

@admin.register(Appointments)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = ['email','first_name','last_name','phone','time','date']


# @admin.register(Appointment)
# class AppointmentAdmin(admin.ModelAdmin):
#
#     list_display = ['email','name','phone_number','time','date']
