# Generated by Django 4.0.3 on 2022-04-14 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heartdisease', models.CharField(choices=[(0, 'No'), (1, 'Yes')], max_length=4, null=True)),
                ('BMI', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True)),
                ('Smoking', models.CharField(choices=[(0, 'No'), (1, 'Yes')], max_length=4, null=True)),
                ('AlcoholDrinking', models.CharField(choices=[(0, 'No'), (1, 'Yes')], max_length=4, null=True)),
                ('Stroke', models.CharField(choices=[(0, 'No'), (1, 'Yes')], max_length=4, null=True)),
                ('PhysicalHealth', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True)),
                ('MentalHealth', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True)),
                ('DiffWalking', models.CharField(choices=[(0, 'No'), (1, 'Yes')], max_length=4)),
                ('Sex', models.CharField(max_length=20)),
                ('AgeCategory', models.CharField(choices=[(1, '18-24'), (2, '24-29'), (3, '30-34'), (4, '35-39'), (5, '40-44'), (6, '45-49'), (7, '50-54'), (8, '55-59'), (9, '60-64'), (10, '65-69'), (11, '70-74'), (12, '75-79'), (13, '80 or older')], max_length=20, null=True)),
                ('Race', models.PositiveIntegerField(null=True)),
                ('Diabetic', models.CharField(choices=[(0, 'No'), (1, 'Yes')], max_length=4, null=True)),
                ('PhysicalActivity', models.CharField(choices=[(0, 'No'), (1, 'Yes')], max_length=4, null=True)),
                ('GenHealth', models.CharField(choices=[(1, 'Poor'), (2, 'Fair'), (3, 'Good'), (4, 'Very good'), (5, 'Excellent')], max_length=4, null=True)),
                ('SleepTime', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True)),
                ('Asthma', models.CharField(choices=[(0, 'No'), (1, 'Yes')], max_length=4)),
                ('KidneyDisease', models.CharField(choices=[(0, 'No'), (1, 'Yes')], max_length=4, null=True)),
                ('SkinCancer', models.CharField(choices=[(0, 'No'), (1, 'Yes')], max_length=4, null=True)),
                ('Predictions', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]