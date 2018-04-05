from django.urls import path
from .views import CreatePatientForm,PatientsList


urlpatterns = [
path('createpatient/',CreatePatientForm.as_view(success_url="/"),name='createpatient'),
path('',PatientsList.as_view(),name='index'),
]