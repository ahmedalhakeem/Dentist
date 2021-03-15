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
        return 
    elif request.method=="GET":
        patient = Add_Patient()
        return render(request, "patientinfo/add_patient.html",{
            "patient" : patient
        })
