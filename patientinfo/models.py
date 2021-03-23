from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass
class Patients(models.Model):
    male = "m"
    female = "f"
    gender_type = [
        (male, "m"),
        (female, "f")
    ]
    name = models.CharField(max_length=64)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=2, choices=gender_type, default=female, null=True, blank=True)
    contact_number = models.IntegerField(null=True, blank=True)
    #appointment = models.ForeignKey(Treatment, on_delete=models.CASCADE, related_name='patient_treat')

    def __str__1(self):
        return f"{self.name}, {self.age}, {self.gender}"

class Extra_appointment(models.Model):
    next_appointment = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)

class Treatment(models.Model):
    patient_name = models.ForeignKey(Patients, on_delete=models.CASCADE, related_name='patient_treat', null=True, blank=True)
    treatment_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    procedure = models.CharField(max_length=100, null=True, blank=True)
    total_cost = models.IntegerField(default=0, null=True, blank=True)
    paid_cost = models.IntegerField(default=0, null=True, blank=True)
    remaining_cost = models.IntegerField(default=0, null=True, blank=True)
    status = models.BooleanField(default=False)
    new_appointment = models.ManyToManyField(Extra_appointment, related_name="extra_appoint")
    def __str__(self):
        return f"{self.procedure}, {self.status}, {self.patient_name}"




