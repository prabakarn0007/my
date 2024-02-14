
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Symptoms_wise_Covid19_Predictor.urls')),
]
