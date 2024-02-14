from django.shortcuts import render
from django.http import HttpResponse
import pickle
import numpy as np


# Load the Random Forest CLassifier model
filename = 'novel-corona-virus-prediction-rfc-model.pkl'
classifier = pickle.load(open(filename, 'rb'))


def home(request):
        return render(request,'index.html')


def predict(request):

      if request.method == 'POST':

        age = int(request.POST.get('age'))
        body_temperature = float(request.POST.get('body_temperature'))

        Gender_Male = request.POST.get('Gender_Male')
        if(Gender_Male == 'Male'):
             Gender_Male = 1
        else:
             Gender_Male = 0

        Dry_Cough_Yes = request.POST.get('Dry_Cough_Yes')
        if(Dry_Cough_Yes == 'Yes'):
             Dry_Cough_Yes = 1
        else:
             Dry_Cough_Yes = 0

        sour_throat_Yes = request.POST.get('sour_throat_Yes')
        if(sour_throat_Yes == 'Yes'):
             sour_throat_Yes = 1
        else:
             sour_throat_Yes = 0

        weakness_Yes = request.POST.get('weakness_Yes')
        if(weakness_Yes == 'Yes'):
             weakness_Yes = 1
        else:
             weakness_Yes = 0

        breathing_problem_Yes = request.POST.get('breathing_problem_Yes')
        if(breathing_problem_Yes == 'Yes'):
             breathing_problem_Yes = 1
        else:
             breathing_problem_Yes = 0

        PIC_Yes = request.POST.get('PIC_Yes')
        if(PIC_Yes == 'Yes'):
             PIC_Yes = 1
        else:
             PIC_Yes = 0

        ICTIP_Yes = request.POST.get('ICTIP_Yes')
        if(ICTIP_Yes == 'Yes'):
             ICTIP_Yes = 1
        else:
             ICTIP_Yes = 0

        diabetes_Yes = request.POST.get('diabetes_Yes')
        if(diabetes_Yes == 'Yes'):
             diabetes_Yes = 1
        else:
             diabetes_Yes = 0

        heart_disease_Yes = request.POST.get('heart_disease_Yes')
        if(heart_disease_Yes == 'Yes'):
             heart_disease_Yes = 1
        else:
             heart_disease_Yes = 0

        lung_disease_Yes = request.POST.get('lung_disease_Yes')
        if(lung_disease_Yes == 'Yes'):
             lung_disease_Yes = 1
        else:
             lung_disease_Yes = 0

        kidney_disease_Yes = request.POST.get('kidney_disease_Yes')
        if(kidney_disease_Yes == 'Yes'):
             kidney_disease_Yes = 1
        else:
             kidney_disease_Yes = 0

        HBP_Yes = request.POST.get('HBP_Yes')
        if(HBP_Yes == 'Yes'):
             HBP_Yes = 1
        else:
             HBP_Yes = 0

        data = np.array([[age, body_temperature, Gender_Male, Dry_Cough_Yes, sour_throat_Yes, weakness_Yes, breathing_problem_Yes, PIC_Yes, ICTIP_Yes, diabetes_Yes, heart_disease_Yes,
                          lung_disease_Yes, kidney_disease_Yes, HBP_Yes]])
        my_prediction = (classifier.predict(data))
        context = {'prediction':my_prediction}
        return render(request,'result.html',context)


