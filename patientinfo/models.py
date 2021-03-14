from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass
class Appointment(models.Model):
    date = models.DateField(auto_now_add=True, blank=True, null=True)

class Treatment(models.Model):
    procedure = models.CharField(max_length=100, null=True, blank=True)
    status = models.BooleanField(default=False)
    treatment_date = models.ManyToManyField(Appointment, related_name="dates")
    total_cost = models.IntegerField()
    remaining_cost = models.IntegerField()

    def __str__(self):
        return f"{self.date},{self.procedure}, {self.status}"




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
    appointment = models.ManyToManyField(Appointment, related_name='patient_treat')

    def __str__1(self):
        return f"{self.name}, {self.age}, {self.gender}"

