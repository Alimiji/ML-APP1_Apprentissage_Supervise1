from django import forms
from .models import Data

"""
self.BMI, self.Smoking, self.AlcoholDrinking,
self.Stroke, self.PhysicalHealth, self.MentalHealth,
self.DiffWalking, self.Sex, self.AgeCategory, self.Race,
self.Diabetic, self.PhysicalActivity, self.GenHealth,
self.SleepTime, self.Asthma, self.KidneyDisease, self.SkinCancer

"""


class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ["BMI", "Smoking", "AlcoholDrinking",
                    "Stroke", "PhysicalHealth", "MentalHealth",
                    "DiffWalking", "Sex", "AgeCategory", "Race",
                    "Diabetic", "PhysicalActivity", "GenHealth",
                    "SleepTime", "Asthma", "KidneyDisease", "SkinCancer"]
