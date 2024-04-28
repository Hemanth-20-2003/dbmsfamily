from django.contrib import admin
from .models import Family,Member,MedicalRecord,Appointment,Medication,Allergy
admin.site.register(Family)
admin.site.register(Member)
admin.site.register(MedicalRecord)
admin.site.register(Appointment)
admin.site.register(Medication)
admin.site.register(Allergy)