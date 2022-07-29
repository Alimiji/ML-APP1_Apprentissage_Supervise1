from django.contrib import admin
from .models import Data

# Register your models here.
"""
self.BMI, self.Smoking, self.AlcoholDrinking,
self.Stroke, self.PhysicalHealth, self.MentalHealth,
self.DiffWalking, self.Sex, self.AgeCategory, self.Race,
self.Diabetic, self.PhysicalActivity, self.GenHealth,
self.SleepTime, self.Asthma, self.KidneyDisease, self.SkinCancer]]

"""

class DataAdmin(admin.ModelAdmin):

    list_display = ('BMI', 'Smoking', 'AlcoholDrinking', 'Stroke', 'PhysicalHealth', 'MentalHealth', 'DiffWalking',
                    'Sex', 'AgeCategory', 'Race', 'Diabetic', 'PhysicalActivity', 'GenHealth', 'SleepTime',
                    'Asthma', 'KidneyDisease', 'SkinCancer', 'Predictions')


admin.site.register(Data, DataAdmin)

