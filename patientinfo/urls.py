from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("main", views.main, name="main"),
    path("logout", views.logout_page ,name="logout_page"),
    path("add_patient", views.add_patient, name="add_patient"),
    path("patient/<int:patient_id>", views.patient, name="patient"),
    path("list_patients", views.list_patients, name="list_patients")
]