from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Family(AbstractUser):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=100)
    emerg_contact = models.CharField(max_length=100)

class Member(models.Model):
    def __str__(self):
        return self.name
    member_id = models.AutoField(primary_key=True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    relationship = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)

class MedicalRecord(models.Model):
    def __str__(self):
        return self.record_id
    record_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date_of_visit = models.DateField()
    doctor_info = models.CharField(max_length=255)
    diagnoses = models.TextField()
    procedures = models.TextField()
    medications = models.ManyToManyField('Medication')
    allergies = models.ManyToManyField('Allergy')
    immunizations = models.TextField()
    notes = models.TextField()

class Appointment(models.Model):
    def __str__(self):
        return self.appointment_id
    appointment_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField()
    provider_info = models.CharField(max_length=255)
    reason = models.TextField()
    notes = models.TextField()

class Medication(models.Model):
    def __str__(self):
        return self.name
    medication_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    side_effects = models.CharField(max_length=255)
    notes = models.TextField()

class Allergy(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    allergy_id = models.AutoField(primary_key=True)
    allergen = models.CharField(max_length=100)
    severity = models.CharField(max_length=100)
    notes = models.TextField()