from django.db import models

from sklearn.linear_model import LogisticRegression
import joblib

# Create your models here.
HeartDisease_RESPONSE = (
    ('Résultat négative', 'No'),
    ('Résultat positive', 'Yes')
)

RESPONSE = (
    (0, 'No'),
    (1, 'Yes')
)

Diabete_Response = (
    (0, 'No'),
    (1, 'Yes'),
    (0, 'No, (borderline diabetes)'),
    (1, 'Yes, (during pregnancy)')
)

GenHealth_Response = (
    (1, 'Poor'),
    (2, 'Fair'),
    (3, 'Good'),
    (4, 'Very good'),
    (5, 'Excellent')
)

Race_Response = (
    (1, 'Hispanic'),
    (2, 'Other'),
    (3, 'American Indian/Alaskan Native'),
    (4, 'Asian'),
    (5, 'Black'),
    (6, 'White')
)

AgeCategory_Response = (
    (1, '18-24'),
    (2, '24-29'),
    (3, '30-34'),
    (4, '35-39'),
    (5, '40-44'),
    (6, '45-49'),
    (7, '50-54'),
    (8, '55-59'),
    (9, '60-64'),
    (10, '65-69'),
    (11, '70-74'),
    (12, '75-79'),
    (13, '80 or older')
)

GENDER = (
    (0, 'Female'),
    (1, 'Male')
)


class Data(models.Model):

    #heartdisease = models.PositiveIntegerField(max_length= 4, choices = RESPONSE, null = True)
    BMI = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=1)
    Smoking = models.PositiveIntegerField(max_length= 4, choices = RESPONSE, null = True)
    AlcoholDrinking = models.PositiveIntegerField(max_length= 4, choices = RESPONSE, null = True)
    Stroke = models.PositiveIntegerField(max_length= 4, choices = RESPONSE, null = True)
    PhysicalHealth = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=1)
    MentalHealth = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=1)
    DiffWalking	 = models.PositiveIntegerField(max_length= 4, choices = RESPONSE)
    Sex	= models.PositiveIntegerField(max_length= 10, choices = GENDER)
    AgeCategory = models.PositiveIntegerField(max_length= 20, choices = AgeCategory_Response, null = True)
    Race = models.PositiveIntegerField(max_length= 20, choices = Race_Response, null = True)
    Diabetic = models.PositiveIntegerField(max_length= 4, choices = RESPONSE, null = True)
    PhysicalActivity = models.PositiveIntegerField(max_length= 4, choices = RESPONSE, null = True)
    GenHealth = models.PositiveIntegerField(max_length= 4, choices = GenHealth_Response, null = True)
    SleepTime = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=1)
    Asthma = models.PositiveIntegerField(max_length= 4, choices = RESPONSE)
    KidneyDisease = models.PositiveIntegerField(max_length= 4, choices = RESPONSE, null = True)
    SkinCancer = models.PositiveIntegerField(max_length= 4, choices = RESPONSE, null = True)
    Predictions = models.CharField(max_length= 100, blank = True)


    def save(self, *args, **kwargs):
        ml_model = joblib.load('modele_prediction/heartdisease_prevision_model.joblib')

        predictions = ml_model.predict([[self.BMI, self.Smoking, self.AlcoholDrinking,
                                              self.Stroke, self.PhysicalHealth, self.MentalHealth,
                                              self.DiffWalking, self.Sex, self.AgeCategory, self.Race,
                                              self.Diabetic, self.PhysicalActivity, self.GenHealth,
                                              self.SleepTime, self.Asthma, self.KidneyDisease, self.SkinCancer]])

        if(predictions[0] == 0):
            self.Predictions = "Résultat négatif"
        else:
            self.Predictions = "Résultat positif"

        return super().save(*args, **kwargs)

    
    def __str__(self):
    
        return str(self.BMI)

    

