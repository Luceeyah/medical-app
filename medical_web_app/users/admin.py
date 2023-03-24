from django.contrib import admin
from .models import User, MedicalRecord, Appointment
# Register your models here.
admin.site.register(User)
admin.site.register(Appointment)

class ProfileAdmin(admin.ModelAdmin):
    list_display=['image','email','stomach_ache', 'malaria', 'injuries', 'head_ache', 'cough', 'fever']
    list_filter=['stomach_ache', 'malaria', 'injuries', 'head_ache', 'cough', 'fever']
    search_fields=['name']

admin.site.register(MedicalRecord , ProfileAdmin)
