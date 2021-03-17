from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import Login_admin, Add_Patient
from .models import *
from django.urls import reverse

# Create your views here.
def index(request):
    if request.method == "POST":
        login_admin = Login_admin(request.POST)
        if login_admin.is_valid():
            username = login_admin.cleaned_data['username']
            password = login_admin.cleaned_data['password']

            login_user = authenticate(request, username=username, password=password)
            if login_user is not None:
                login(request, login_user)
                return HttpResponseRedirect(reverse('main'))
            else:
                return HttpResponse('invalid login')
    else:
        login_page = Login_admin()
        return render(request, 'patientinfo/index.html',{
            "login_admin": login_page
        })

def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

@login_required
def main(request):
    return render(request, 'patientinfo/main.html')

def add_patient(request):
    if request.method == "POST":
        patient = Add_Patient(request.POST or None)
        if patient.is_valid():
            name = patient.cleaned_data['name']
            age = patient.cleaned_data['age']
            gender = patient.cleaned_data['gender']
            contact = patient.cleaned_data['contact']

            #save it in the database
            new_patient = Patients(name=name, age=age, gender=gender, contact_number=contact)
            for item in Patients.objects.all():
                if (new_patient.name == item.name):
                    return render(request, 'patientinfo/add_patient.html',{
                        "message": "هذا الاسم تم ادخاله مسبقا في النظام"
                    }) 
                else:
                    new_patient.save()
            
                    return HttpResponseRedirect(reverse('patient' ,args=(new_patient.pk,)))
    elif request.method=="GET":
        patient = Add_Patient()
        return render(request, "patientinfo/add_patient.html",{
            "patient" : patient
        })

def patient(request, patient_id):
    patient = Patients.objects.get(pk=patient_id)
    return render(request, 'patientinfo/patient_profile.html',{
        "patient" : patient
    })
def list_patients(request):
    all_patients = Patients.objects.all()
    return render(request, 'patientinfo/list_patients.html',{
        "list_patients": all_patients
    })